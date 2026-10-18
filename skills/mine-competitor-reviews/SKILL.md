---
name: mine-competitor-reviews
description: Finds an app's competitors, mines their App Store / Google Play reviews, clusters and counts the complaints and requests, and turns the strongest into one mini-report per problem tailored to the user's own app — with a "do this week" decision, confidence labels, and a plain-language reading guide — delivered as a shareable report plus a readable review table. Use whenever the user wants competitor analysis from reviews, feature gaps, "what do users hate about X", "rakip analizi", "rakip uygulamanın kötü yorumları", review mining, or is planning features for an app and wants to learn from rivals — even if they name no competitor (this skill finds them) or never say "report".
---

# Mine competitor reviews

Turn what users complain about and ask for in competing apps into a short, evidence-backed plan for the user's own app.

Two things make this worth more than a list of plausible features. Every recommendation traces back to real, counted reviews: how many people hit the problem, how badly it pushed them away, whether solving it fits the user's app. And the report is written for a busy founder who may never have read one like it: the decision comes first, every number says how much to trust it, and no term goes unexplained.

## 0. Tell the user what will happen

Before the first tool call, send one short message (in the user's language) so nothing that follows surprises them:

- what you'll ask (their app in a sentence or two, the market) and that they don't need to know their competitors — you'll suggest some, and they can say "you pick" to skip that step;
- roughly how long it takes (usually 15–25 minutes; they can step away);
- that you'll open Google Play in a browser to read public reviews, so they may see a request to allow it — read-only, no sign-in, nothing posted;
- that Apple doesn't let tools read App Store complaints automatically, so App Store is covered only if they want: a few iPhone screenshots, a review-tool CSV, an Apify connector, or a Mac — you'll ask once;
- what they'll get: a report that starts with what to do this week, plus a table of every review used.

## 1. Gather inputs

- **The user's own app**: what it does, who it's for, its stage, and its key product decisions (pricing model, what it deliberately does differently). Check the conversation and memory first; ask only for what's missing, in one question. These decisions matter later: a competitor's complaint can reveal that one of the user's own choices is risky.
- **Market**: store country/language. Default to the user's country.
- **Competitors**: 1–3. The user may name them; if not, find them (below).

If the user's app context is unknown and they aren't around to answer, proceed with general opportunities and say so at the top of the report.

### Finding competitors

From the app description, derive 3–5 phrases a target user would type into a store, in the market's language. Search the web for them on apps.apple.com and play.google.com, plus "best <category> app <year>". If a browser is available, the store's own search page (`https://play.google.com/store/search?q=<phrase>&c=apps&hl=<lang>&gl=<country>`) gives a much better list than web search — new niche apps rarely rank on Google yet.

Shortlist 4–6, then pick 2–3 by: overlap in core job and audience; review volume (enough written reviews to analyze); presence in the target market; and **still being listed** — open each listing before committing, because removed apps still show up in search results. Prefer one category leader plus one or two closer rivals.

**Confirming the picks.** A wrong competitor wastes the whole run, so the user gets one chance to swap — but it should cost them at most one tap:

- **Skip the question entirely** when the user named their competitors, said to choose for them ("you pick", "sen seç", "just run it"), or isn't around (scheduled run, said they'd check back, an earlier question went unanswered). Proceed with your picks and state them, with reasons, at the top of your next message and in the report.
- **Otherwise ask once**, as a single multiple-choice question when the session has one (AskUserQuestion): the first option is your recommended set, labeled "(Recommended)", so confirming is one tap; one or two alternative sets as the other options (e.g. direct rivals only, or leader plus closest rival). Put the full shortlist with a one-line reason per app in the question text. Without a question tool, list the shortlist and say you'll go with the recommended set unless they reply with changes — and proceed if they don't.

**App Store coverage.** Ask how to include App Store complaints — as a second question in the same call, or on its own if the competitor question was skipped because the user named them. Skip it only if the user is away (then: Google Play only) or already said. Options, in this order, keeping only those that apply:
- "Google Play only" — the default when nothing else is available; mark it "(Recommended)" if the competitors are Android-heavy or the user seems short on time;
- "I'll send iPhone screenshots of <App> (about 5)" — always available (route A in `references/collection.md`). Ask for **one competitor only**: the one where App Store matters most — iOS-only, a much larger App Store rating count than on Google Play, or the leader on iOS. Name it and the reason in the option's description (e.g. "Forest has 5× more ratings on iOS than on Play"), so the user knows why that app and that it's just one. They can still send more apps or more images if they want;
- "I have a review-tool CSV" (route B);
- "Use Apify" — only if Apify tools are present in the session (route C; it costs the user credits, so it still needs a yes on the price before running);
- "Use my Mac" — only if computer use is available and the computer is a Mac (route D).
If the user chooses screenshots or CSV, give the short instructions (for screenshots: which app, why that one, and that about 5 images are enough) and carry on with Google Play while they gather them; merge their files when they arrive. If they don't arrive before the report is ready, publish without them and say App Store wasn't covered.

If a pick turns out to be removed or empty during collection, replace it with the next-best candidate and tell the user in one message rather than stopping. Keep the shortlist and the reasons: they go in the report.

## 2. Collect reviews

Target written reviews from the last 12–24 months. Read `references/collection.md` before collecting — it has the store-specific mechanics that work and the ones that don't. In short:

- **Google Play** is the reliable source, but only through a browser: the listing page shows 3 reviews, and the "See all reviews" dialog loads more only on real mouse-wheel scrolling. The reference file has the extraction script and the star-filter steps.
- **App Store**: Apple's review RSS feed and search API are refused by fetch tools (robots), and the web listing shows only ~20 "most helpful" reviews with no filter — don't work around the refusal. Record each competitor's App Store rating, then use the route the user chose (screenshots, CSV, Apify, or Mac; see `references/collection.md`). With none, say App Store complaints weren't covered.
- **Supplementary web** (Reddit, forums) only when store data is thin; mark the source on each row.

Save every review to `reviews.csv` with columns: `id, competitor, source, country, rating, date, version, title, text, url, themes, churn_signal`. Give each row a short stable id (`K12`, `G4`) — the report cites these instead of long quotes.

Record, per competitor, how many reviews the store says exist versus how many you loaded. That ratio goes in the report.

## 3. Decide what to analyze

Count 1–3★ written reviews first.

- **Enough negatives (roughly 30+ per competitor)**: analyze them as the core set; use 4–5★ requests as supporting evidence.
- **Few negatives** (common for young niche apps with 4.5★+ ratings): also mine **requests and complaints inside 4–5★ reviews** ("great, but…", "if only it had…", "please don't make it paid"). Say plainly in the report that the findings come mostly from satisfied users' wish lists, which is a different signal from churn.

Drop reviews with no actionable content ("bad", "5 stars"). Note app versions; a spike tied to one version is usually a bug, not a gap.

## 4. Tag and count

Read the reviews and tag each with one or more themes. Let themes emerge from the text, then merge synonyms into roughly 8–15. **Name themes in plain words in the report's language** — even when the reviews are in another language ("Adding questions one by one is tedious", not `BULK_ADD`): these names appear in the CSV the user opens, so a code nobody can read defeats the table. Keep names short enough to fit a column (under ~60 characters) and use exactly the same string every time.

Give each theme a type, because the type changes what the user should do:

| Type | Meaning | Usually means for the user |
|---|---|---|
| Missing feature | Users want something the app doesn't do | Direct feature opportunity |
| Bug | Exists but fails | Reliability as a differentiator; competitor may fix it soon |
| UX friction | Works but tedious or confusing | Design opportunity, often cheap |
| Pricing | Price, limits, paywalls, ads, fear of going paid | Positioning and monetization input |
| Trust | Data loss, privacy, account, support | Messaging, policy, and architecture input |

Mark `churn_signal` (`yes`) on reviews where the user says they left, switched, uninstalled, recommend an alternative, or that friends refused to adopt it.

Compute counts with `scripts/count_themes.py reviews.csv` — never by eye. It reports per theme: count, share of tagged reviews, count among 1–3★, churn signals, last-12-months count, number of competitors, per-competitor split, and a **confidence** label. When the report combines themes ("data loss and sync together appear in N reviews"), use the script's `--union` option with themes separated by `;` (names often contain commas), because one review can carry both tags and adding the two counts overstates it. If the script warns that a name wasn't found, fix the spelling before using the number.

### Confidence

The script labels each theme so readers know how much weight a number can bear:

- **Strong**: 10+ reviews from 2+ competitors, or 6+ reviews with at least one churn signal (from 2+ competitors unless there are 10+ reviews).
- **Medium**: 5–9 reviews, or any churn signal behind fewer. A theme seen at only one competitor with under 10 reviews never rates above Medium.
- **Weak**: under 5 reviews and no churn signal.

You may move a label one step with a stated reason (e.g. a single review that names a data-loss incident in detail). Show the label wherever the theme's numbers appear.

## 5. Score and judge fit

For each theme weigh frequency, churn signals, recency (a theme that's all old reviews is likely fixed), confidence, and **fit**: how naturally solving it fits the user's app (high / medium / low, one-line reason). A frequent complaint that clashes with the user's product philosophy is not their opportunity.

Also check the reverse: does any frequent fear or complaint collide with one of the user's own planned decisions? (Example: users of rivals fear losing their saved photos, while the user's app plans to auto-delete photos after a step.) Surface these as warnings; they are often the most valuable line in the report.

Watch for **release backlash**: when most of a theme's reviews come from one competitor within a few weeks (check the dates), it's a reaction to one release, not a standing gap. Say so in the theme's row and mini-report, and take the lesson (e.g. a tap limit) rather than the feature list.

Rank by frequency × churn × recency, filtered by fit. Explain rankings in plain words so the user can disagree with a specific judgment.

## 6. One mini-report per problem

Pick the 3–6 strongest problems. Write each as its own self-contained mini-report, so a reader can read just that one and understand what's wrong, how we know, how sure we are, what to build and why each piece is there. Every mini-report uses the same fields, in this order, as bullets:

1. **Problem**: one or two sentences in the users' own terms, with the numbers (count, share, 1–3★ count, churn signals, competitors affected).
2. **Confidence**: Strong / Medium / Weak, with the count behind it ("Medium: 7 reviews, one competitor").
3. **Why it's ranked here**: one line naming what put it at this position — frequency, churn, recency, fit, or a collision with the user's own plans.
4. **Evidence**: 2–4 reviews as sub-bullets, each paraphrased in a clause with id, rating and month (`G20, 4★, Oct 2026`). Keep any direct quote to a few words, at most one per mini-report; full text lives in the review table. Add one sub-bullet on what the user's own app does today when it's known (code, flow, or plan), since that's what turns a rival's problem into the user's risk or opportunity.
5. **Proposal**: the fix broken into its parts, one sub-bullet per part. Every part states **what** to build and **why** — the evidence id(s) it answers, or a product reason — e.g. "Store an end timestamp and recompute on return — *because the timer freezes in the background (T10, T26).*" A part with no review behind it is labeled "*no review evidence; supporting change*" so the reader can cut it. Mark each part Must / Should / Later.
6. **Fit**: high / medium / low, tied to the user's audience, stack and flows; name any tension with their existing decisions.
7. **Effort**: S / M / L for one developer, labeled a rough guess — S = 1–2 days, M = about a week, L = two weeks or more.
8. **Store line**: one line for the listing or an ad.
9. **Validate first**: the cheapest check and what result means go / no-go.

Number the mini-reports in rank order and title each by the problem, not the solution ("1. The timer stops when the phone is locked", not "1. Background-proof timer").

Then a short **Don't chase** list: frequent but old bugs, scope creep into adjacent products, niche requests, things that contradict the user's positioning — each with its one-line reason.

## 7. The decision at the top

Write this last, from the mini-reports, and put it first in the report. Most readers stop here, so it must stand alone:

- **One sentence**: what to do and why, in plain words.
- **This week**: up to 3 concrete actions, each pointing to its mini-report number, each small enough to start now (often the "validate first" step, a quick fix, or a warning to act on).
- **Watch out**: the collision with the user's own plans, if one was found.

No numbers that need the reading guide to understand; say "the most common request among recent reviews" rather than "28%, Medium".

## 8. Deliver

Publish the report as a shareable document: the Docs artifact type or docs connector when the session offers one, otherwise a clean HTML artifact, otherwise markdown. Write in the language of the user's request.

Structure:

```
# <App> competitor analysis: <competitors>
## What to do (step 7: one sentence, this week, watch out)
## Summary (3–5 bullets: biggest opportunities, any warning, sample size)
## Who we compared against (each competitor: why chosen, what it does, rating, price model; then the candidates left out and why, one line each)
## Data (table: competitor, store, reviews loaded vs total, 1–3★ count, date range, route for App Store; then caveats)
## What users complain about (chart + table, see below)
## Problems and proposals (one numbered subsection per problem, titled by the problem, fields 1–9 from step 6 in order)
## Don't chase
## How to read this report (glossary box, see below)
## Method & limitations
```

**Complaint themes as a chart.** When the document supports charts, draw theme counts as a horizontal bar chart sorted by count: bars grey, the themes that became mini-reports in one accent colour (if that's more than about half the bars, accent only the themes behind the "This week" actions so the colour still points somewhere), the confidence label at the end of each bar, the finding in the title. The table under it lists type, 1–3★, churn, last 12 months, competitors and fit — without repeating the counts the chart already shows. Without chart support, use one table with all columns.

**How to read this report.** A short box near the end, in plain words, defining only the terms the report actually uses — typically: 1–3★ (reviews rated one to three stars), churn signal (the reviewer says they left, switched or won't use it), confidence (Strong / Medium / Weak and what makes each), fit, Must / Should / Later, effort S / M / L in days, review ids (`G20` = row G20 in the review table), "last 12 months".

**Review table.** Send `reviews.csv` with the plain-language theme names. When the session offers a Sheets (spreadsheet) artifact type, also publish the reviews there so the user can filter by competitor, rating and theme without opening a file; link it from the Data section.

Limitations always state: negative reviews are a skewed sample; counts cover only what the stores exposed (loaded vs total); which stores were covered and how (e.g. "App Store: 34 reviews from the user's screenshots, sorted Most Critical") or not at all.

Before handing off, re-check every number in the text against the script output, every cited id against the CSV, every proposal part for its "why", and every mini-report for its confidence label. Then reread the "What to do" section as someone who will read nothing else.

## Finishing

In chat: two lines — the single biggest opportunity (plus any warning about the user's own plans) and the sample size — then point to the report. Offer the natural next step: turning a problem's proposal into a spec with the `gap-to-spec` skill.
