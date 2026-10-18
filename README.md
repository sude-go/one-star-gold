# One Star Gold

*Your competitor's one-star review is your roadmap.*

One Star Gold turns what users complain about in competing apps into evidence-backed decisions — and then build-ready specs — for your own app. Made for indie hackers, solo founders and small product teams who'd rather build what users are already asking for.

## Quick start

1. Install the plugin.
2. Say: *"Run a competitor analysis for my app"* and describe your app in a sentence or two. You don't need to know your competitors: Claude suggests 2–3 and you confirm with one tap — or add "you pick" to skip that step.
3. Allow Google Play (and the App Store) in the browser when asked. Claude only reads public reviews — no sign-in, nothing posted.
4. Wait 15–25 minutes. You can step away.
5. Read the **What to do** section at the top of the report. That's the decision; everything below is the evidence.

Then: *"Turn problem 1 into a spec."*

## What you get

**A report that starts with the decision**

- **What to do** — one sentence and up to three actions for this week, plus any warning about your own plans.
- **Who we compared against** — the competitors chosen, why, and which candidates were left out.
- **What users complain about** — a chart of every theme, with how much to trust each.
- **One mini-report per problem**, always in the same order:
  1. Problem — in users' terms, with numbers
  2. Confidence — Strong / Medium / Weak, and how many reviews it rests on
  3. Why it's ranked here
  4. Evidence — reviews by id, plus what your app does today
  5. Proposal — the fix in parts; every part says what to build and *why*, Must / Should / Later
  6. Fit with your app · 7. Effort (S = 1–2 days, M ≈ 1 week, L = 2+ weeks) · 8. Store line · 9. What to validate first
- **Don't chase** — popular requests you should ignore, and why.
- **How to read this report** — every term in plain words.

**A review table** — every review used, with plain-language theme names, as a CSV (and a filterable sheet when available).

**A spec on request** (`gap-to-spec`) — goal and non-goals, flow, requirements traced to review ids, edge cases, acceptance criteria, a success metric tied to the original complaint, and a validation gate.

### Example (excerpt from a real run)

> **1. Adding questions one at a time is tedious**
> - **Problem:** The most repeated request in one rival's recent reviews: 7 reviews, all from the last four months.
> - **Confidence:** Medium — 7 reviews, one competitor.
> - **Why it's ranked here:** Recent, consistent, and it hits the app's main action.
> - **Evidence:** G1 (5★, Sep 2026) wants to pick several photos from the gallery at once · G4 (5★, Sep 2026) re-enters subject, topic and note for every question · G20 (4★, Oct 2026) wants all mistakes from one test tagged in one go.
> - **Proposal:**
>   - Batch capture mode after one subject/topic pick — *because tagging every question again is the core complaint (G4, G20).* Must
>   - Multi-select from the gallery into the same flow — *because users screenshot questions (G1).* Must
>   - Per-question edit of the shared tag — *no review evidence; supporting change so batch tagging isn't a trap.* Should
> - **Fit:** High · **Effort:** S–M · **Store line:** "Add 10 mistakes in a minute." · **Validate first:** time a 5-question add against rivals.

## How it works

- Every number comes from a script run over the review table, not from eyeballing.
- Every proposal part cites the reviews behind it, so you can read the originals.
- Reports are written in the language you ask in.
- When competitors have mostly happy reviews (common for young niche apps), it mines the "great, but…" requests in 4–5★ reviews and says so.

## Including the App Store

Apple doesn't let tools read App Store complaints automatically: its review feeds block automated access, and the web page shows only about 20 "most helpful" reviews with no sorting. Claude asks once how you'd like to cover it:

| Route | Cost | What you do |
| --- | --- | --- |
| **iPhone screenshots** | Free, ~5 minutes | Claude asks for **one** competitor — the one where the App Store matters most — and tells you why. Open it in the App Store app → Ratings & Reviews → See All → sort by **Most Critical**, take about 5 screenshots and attach them. Claude transcribes them into the review table. |
| **Review-tool CSV** | Free if you already use one | Export competitor reviews from AppFollow, Appfigures, AppTweak or similar and attach the file. |
| **Apify connector** | Your Apify credits (small runs fit the free tier) | Add Apify once: Settings → Connectors → Add custom connector → `https://mcp.apify.com` (OAuth sign-in). Claude tells you the cost and waits for your yes before each run. |
| **Mac App Store** | Free, macOS only | On an Apple Silicon Mac with computer use, Claude reads the Mac App Store's iPhone app reviews itself, read-only. |

Google Play collection continues while you gather screenshots or a CSV; they're merged when they arrive.

## Limits

- **A browser tool is strongly recommended** (Claude's built-in browser or Claude in Chrome). Google Play shows full review lists only in a browser.
- **App Store** needs one extra step — see below. Without it, the report covers Google Play only and says so.
- Samples are only as large as what the stores show; the report states reviews loaded vs total.
- Reviews are a skewed sample. Treat findings as strong hypotheses and run the suggested validation before a big build — especially for anything marked Weak.

## Files

```
skills/mine-competitor-reviews/   competitor discovery, collection, tagging, scoring, report
  references/collection.md        store-specific collection mechanics
  scripts/count_themes.py         theme counts, churn, recency, confidence, unions
skills/gap-to-spec/               problem → spec
```


## License

MIT. Made by Meryem Sude Gök.
