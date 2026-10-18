#!/usr/bin/env python3
"""Count themes in a tagged reviews.csv.

Usage:
  python3 count_themes.py reviews.csv [--since YYYY-MM-DD] [--union 'THEME A;THEME B' ...] [--json out.json]

reviews.csv needs at least: id, competitor, rating, date (YYYY-MM-DD), themes (';'-separated), churn_signal ('yes' or empty).
--since defaults to 12 months before the newest review date.
--union prints how many distinct reviews carry ANY of the listed themes (use it whenever the report adds themes together).
  Separate themes with ';' — the same separator as the themes column — because plain-language theme names may contain commas.
"""
import argparse, csv, json
from collections import Counter
from datetime import date, timedelta


def parse_date(s):
    try:
        y, m, d = (int(x) for x in s.split('-'))
        return date(y, m, d)
    except Exception:
        return None


def confidence(n, churn, comps):
    """Strong: 10+ reviews from 2+ competitors, or 6+ with a churn signal.
    Medium: 5-9 reviews, or any churn signal. Weak: otherwise.
    One competitor with under 10 reviews never rates above Medium."""
    if (n >= 10 and comps >= 2) or (n >= 6 and churn >= 1 and (comps >= 2 or n >= 10)):
        return 'Strong'
    if n >= 5 or churn >= 1:
        return 'Medium'
    return 'Weak'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('csv')
    ap.add_argument('--since')
    ap.add_argument('--union', action='append', default=[])
    ap.add_argument('--json')
    a = ap.parse_args()

    rows = list(csv.DictReader(open(a.csv, encoding='utf-8')))
    for r in rows:
        r['_themes'] = {t.strip() for t in (r.get('themes') or '').split(';') if t.strip()}
        r['_date'] = parse_date(r.get('date') or '')
        try:
            r['_rating'] = int(r.get('rating') or '')
        except ValueError:
            r['_rating'] = None
        r['_churn'] = (r.get('churn_signal') or '').strip().lower() in ('yes', 'y', '1', 'true')

    dates = [r['_date'] for r in rows if r['_date']]
    since = parse_date(a.since) if a.since else ((max(dates) - timedelta(days=365)) if dates else None)

    tagged = [r for r in rows if r['_themes']]
    neg = [r for r in rows if r['_rating'] is not None and r['_rating'] <= 3]
    recent = lambda r: bool(since and r['_date'] and r['_date'] >= since)

    summary = {
        'rows': len(rows),
        'rows_per_competitor': Counter(r['competitor'] for r in rows),
        'rated_1_3': len(neg),
        'rated_1_3_per_competitor': Counter(r['competitor'] for r in neg),
        'tagged': len(tagged),
        'tagged_per_competitor': Counter(r['competitor'] for r in tagged),
        'churn_signals': sum(r['_churn'] for r in rows),
        'recent_since': since.isoformat() if since else None,
    }

    themes = sorted({t for r in tagged for t in r['_themes']})
    table = []
    for t in themes:
        hits = [r for r in tagged if t in r['_themes']]
        n, churn = len(hits), sum(r['_churn'] for r in hits)
        comps = len({r['competitor'] for r in hits})
        table.append({
            'theme': t,
            'count': n,
            'share_of_tagged_pct': round(100 * n / len(tagged)) if tagged else 0,
            'rated_1_3': sum(1 for r in hits if r['_rating'] is not None and r['_rating'] <= 3),
            'churn': churn,
            'recent': sum(recent(r) for r in hits),
            'competitors': comps,
            'confidence': confidence(n, churn, comps),
            'by_competitor': dict(Counter(r['competitor'] for r in hits)),
            'ids': [r['id'] for r in hits],
        })
    table.sort(key=lambda x: (-x['count'], -x['churn'], -x['rated_1_3']))

    unions = {}
    for spec in a.union:
        ts = {x.strip() for x in spec.split(';') if x.strip()}
        unknown = ts - set(themes)
        if unknown:
            print(f"warning: --union names not found in themes column: {sorted(unknown)}")
        unions[spec] = sum(1 for r in tagged if r['_themes'] & ts)

    print(json.dumps(summary, ensure_ascii=False, default=dict))
    w = max([len(x['theme']) for x in table] + [5]) + 2
    print(f"{'theme':<{w}}{'n':>4}{'%':>5}{'1-3*':>6}{'churn':>7}{'recent':>8}{'comps':>7}  {'confidence':<11}by competitor")
    for x in table:
        print(f"{x['theme']:<{w}}{x['count']:>4}{x['share_of_tagged_pct']:>5}{x['rated_1_3']:>6}{x['churn']:>7}{x['recent']:>8}{x['competitors']:>7}  {x['confidence']:<11}{x['by_competitor']}")
    for k, v in unions.items():
        print(f"union[{k}] = {v} distinct reviews")

    if a.json:
        json.dump({'summary': summary, 'themes': table, 'unions': unions}, open(a.json, 'w', encoding='utf-8'),
                  ensure_ascii=False, indent=1, default=dict)


if __name__ == '__main__':
    main()
