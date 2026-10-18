# Changelog

## 0.3.1 — 2026-10-18
- App Store screenshots: ask for one competitor (the one where the App Store matters most) and about 5 images, and say why that one.

## 0.3.0 — 2026-10-18
- Four ways to include App Store complaints: iPhone screenshots, a review-tool CSV, an Apify connector (with a cost confirmation), or the Mac App Store via computer use.
- Data table split by store, with the App Store route used.

## 0.2.3 — 2026-10-18
- Fixed `--union` in `count_themes.py`: themes are now separated by `;` (theme names can contain commas), with a warning for unknown names.
- Theme names follow the report's language even when reviews are in another language.
- Detects "release backlash" (one competitor, one release, a few weeks).
- Google Play: English star-filter labels, more scrolling for long reviews. App Store web page documented as unusable for complaints.

## 0.2.2 — 2026-10-18
- Competitor confirmation is one tap (recommended set pre-selected) and skipped when the user names competitors, says "you pick", or is away.

## 0.2.0 — 2026-10-18
- "What to do" section first, confidence labels (Strong / Medium / Weak), a plain-language reading guide, readable theme names, a kickoff message, competitor selection reasons, and a theme chart.

## 0.1.1 — 2026-10-18
- One mini-report per problem; every proposal part states what to build and why.

## 0.1.0 — 2026-10-18
- First release: `mine-competitor-reviews` and `gap-to-spec`.
