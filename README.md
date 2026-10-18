<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg">
    <img src="assets/banner-light.svg" alt="One Star Gold — your competitor's one-star review is your roadmap." width="640">
  </picture>
</p>

<p align="center">
  <a href="https://github.com/sude-go/one-star-gold/releases"><img src="https://img.shields.io/github/v/release/sude-go/one-star-gold?color=E8A317&label=release" alt="Latest release"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-1F1A10" alt="MIT license"></a>
  <img src="https://img.shields.io/badge/Claude-plugin-C98400" alt="Claude plugin">
  <img src="https://img.shields.io/badge/Google%20Play%20%2B%20App%20Store-reviews-6B5E45" alt="Google Play and App Store reviews">
</p>

<p align="center">
  <b>Turn your competitors' app store complaints into evidence-backed decisions — and build-ready specs — for your own app.</b><br>
  For indie hackers, solo founders and small product teams who'd rather build what users are already asking for.
</p>

<p align="center">
  <a href="#install">Install</a> ·
  <a href="#quick-start">Quick start</a> ·
  <a href="#what-you-get">What you get</a> ·
  <a href="#including-the-app-store">App Store</a> ·
  <a href="#limits">Limits</a> ·
  <a href="CHANGELOG.md">Changelog</a>
</p>

---

## Why

Every one-star review of a competitor is a user telling you, for free, what would have kept them. The hard part isn't reading reviews — it's counting them honestly, knowing how much to trust a pattern, and turning it into something you can ship this week without chasing every request.

One Star Gold does that end to end inside Claude: it finds your competitors, reads their reviews, counts what hurts, checks the findings against your own product decisions, and starts the report with what to do.

## Install

**Claude Code** (terminal, desktop app, VS Code) — one command, Claude Code v2.1.275 or later:

```text
/plugin install one-star-gold --marketplace sude-go/one-star-gold
```

Or in two steps, from your shell:

```bash
claude plugin marketplace add sude-go/one-star-gold
claude plugin install one-star-gold@one-star-gold
```

In the desktop app you can also use **+ → Plugins → Add plugin** after adding the marketplace.

**Claude app (claude.ai / Cowork)** — download `one-star-gold.plugin` from the [latest release](https://github.com/sude-go/one-star-gold/releases/latest) and add it as described in Anthropic's guide to [plugins on claude.ai and in Cowork](https://claude.com/docs/plugins/overview).

**Updates** — run `claude plugin update one-star-gold@one-star-gold`, or turn on auto-update for this marketplace in `/plugin` → **Marketplaces**.

## Quick start

1. Say: *"Run a competitor analysis for my app"* and describe your app in a sentence or two. You don't need to know your competitors: Claude suggests 2–3 and you confirm with one tap — or add *"you pick"* to skip that step.
2. Allow Google Play in the browser when asked. Claude only reads public reviews — no sign-in, nothing posted.
3. Optionally include the App Store ([see below](#including-the-app-store)).
4. Wait 15–25 minutes. You can step away.
5. Read **What to do** at the top of the report. That's the decision; everything below is the evidence.

Then: *"Turn problem 1 into a spec."*

Both skills can also be called by name: `/one-star-gold:mine-competitor-reviews` and `/one-star-gold:gap-to-spec`.

## What you get

### A report that starts with the decision

- **What to do** — one sentence and up to three actions for this week, plus any warning about your own plans.
- **Who we compared against** — the competitors chosen, why, and which candidates were left out.
- **What users complain about** — a chart of every theme with how much to trust each, and a table of type, churn signals, recency and fit.
- **One mini-report per problem**, always in the same order:
  1. **Problem** — in users' terms, with numbers
  2. **Confidence** — Strong / Medium / Weak, and how many reviews it rests on
  3. **Why it's ranked here**
  4. **Evidence** — reviews by id, plus what your app does today
  5. **Proposal** — the fix in parts; every part says what to build and *why*, marked Must / Should / Later
  6. **Fit** with your app · 7. **Effort** (S = 1–2 days, M ≈ 1 week, L = 2+ weeks) · 8. **Store line** · 9. **Validate first**
- **Don't chase** — popular requests you should ignore, and why.
- **How to read this report** — every term in plain words.

### A review table

Every review used, with plain-language theme names and churn signals, as a CSV — so every number in the report can be checked.

### A spec on request

`gap-to-spec` turns a problem into a short spec: goal and non-goals, flow, requirements traced to review ids, edge cases, acceptance criteria, a success metric tied to the original complaint, and a validation gate.

### Example

An excerpt from a real run for a focus-timer app, using public Google Play reviews of large competitors:

> **1. The timer stops or miscounts when the phone is locked**
> - **Problem:** Focused time gets lost: the timer stops in the background, freezes, or records the wrong duration. 17 one-star reviews of one competitor, all from the last 12 months.
> - **Confidence:** Medium — 17 reviews, but one competitor.
> - **Why it's ranked here:** It's the app's core job, and the user's own timer had the same design risk.
> - **Evidence:** T44 (1★, Jun 2026) timer shuts itself off in the background after a few minutes · T48 (1★, May 2026) a 90-minute session froze at 66 · T22 (1★, Aug 2026) stuck between phases, no minutes recorded · *Your app today:* a one-second interval that decrements state.
> - **Proposal:**
>   - Store an end timestamp and recompute on return — *because the timer stops in the background (T44, T48).* **Must**
>   - Record duration from the same timestamps — *because users lose the minutes they worked (T22, T25).* **Must**
>   - One local notification at the end — *no review evidence; supporting change so a locked phone still signals the end.* **Should**
> - **Fit:** High · **Effort:** S–M · **Store line:** "Lock your phone. It keeps counting." · **Validate first:** a 25-minute locked-screen session against a stopwatch.

## How it works

1. **Find competitors** — searches the stores from your app's description, checks each listing is live, and picks 2–3 (one leader, one or two close rivals).
2. **Collect reviews** — reads Google Play's full review lists in a browser, newest first, filtered to low ratings.
3. **Tag and count** — groups complaints into plain-language themes; a bundled script counts them, labels confidence, and computes overlaps so combined numbers are never double-counted.
4. **Judge** — weighs frequency, churn signals, recency and fit; flags one-release backlashes and collisions with your own plans.
5. **Report** — writes the decision first, then the evidence, in the language you asked in.

When competitors have mostly happy reviews (common for young niche apps), it mines the "great, but…" requests in 4–5★ reviews and says so.

## Including the App Store

Apple doesn't let tools read App Store complaints automatically: its review feeds block automated access, and the web page shows only about 20 "most helpful" reviews with no sorting. Claude asks once how you'd like to cover it:

| Route | Cost | What you do |
| --- | --- | --- |
| **iPhone screenshots** | Free, ~5 minutes | Claude asks for **one** competitor — the one where the App Store matters most — and tells you why. Open it in the App Store app → Ratings & Reviews → See All → sort by **Most Critical**, take about 5 screenshots and attach them. Claude transcribes them into the review table. |
| **Review-tool CSV** | Free if you already use one | Export competitor reviews from AppFollow, Appfigures, AppTweak or similar and attach the file. |
| **Apify connector** | Your Apify credits | Add Apify once: Settings → Connectors → Add custom connector → `https://mcp.apify.com` (OAuth sign-in). Claude tells you the cost and waits for your yes before each run. |
| **Mac App Store** | Free, macOS only | On an Apple Silicon Mac with computer use, Claude reads the Mac App Store's iPhone app reviews itself, read-only. |

Google Play collection continues while you gather screenshots or a CSV; they're merged when they arrive.

## Requirements

- Claude with a **browser tool** — Claude's built-in browser (desktop app) or Claude in Chrome. Google Play shows full review lists only in a browser.
- Python 3 in Claude's environment for the counting script (standard library only).
- Optional: Apify connector or a Mac with computer use for automated App Store coverage.

## Limits

- **App Store** needs one extra step (above). Without it, the report covers Google Play only and says so.
- Samples are only as large as the stores show; the report states reviews loaded vs total.
- Reviews are a skewed sample: angry users write more, quiet churners don't write at all. Treat findings as strong hypotheses and run the suggested validation before a big build — especially for anything marked Weak.

## Privacy and safety

- Reads public store pages only. It never signs in, rates, posts or reports.
- Review text is treated as data; instructions inside a review are ignored.
- Apify runs only after you approve the cost. Nothing is sent to third parties otherwise.

## Repository layout

```
.claude-plugin/
  plugin.json                     manifest
  marketplace.json                lets this repo act as its own marketplace
skills/
  mine-competitor-reviews/        competitor discovery, collection, tagging, scoring, report
    references/collection.md      store-specific collection mechanics and App Store routes
    scripts/count_themes.py       theme counts, churn, recency, confidence, overlaps
  gap-to-spec/                    problem → spec
assets/                           logo, banners, social preview
```

## Contributing

Bug reports and ideas are welcome — see [CONTRIBUTING.md](CONTRIBUTING.md). The most useful reports include the app category, store and country, and what the report got wrong.

## License

[MIT](LICENSE) © 2026 Meryem Sude Gök
