---
name: gap-to-spec
description: Turns a feature opportunity found in competitor reviews (usually a proposal from a mine-competitor-reviews report) into a build-ready feature spec for the user's own app, with the review evidence carried through to goals, acceptance criteria and success metrics. Use when the user says "turn proposal 2 into a spec", "spec this feature", "write a PRD for the bulk-add idea", "bunu spec'e çevir", or wants to move from a competitor-review finding to something they can build.
---

# Gap to spec

Turn one opportunity into a spec a solo founder or small team can build from this week. The spec's value over a generic PRD is that every goal and metric is anchored in what real users of competing apps said, so scope arguments can be settled by evidence.

## 1. Find the source

- If a competitor-review report exists in this conversation or the user links one, read it and the problem they mean. Pull its numbers, review ids, the proposal parts with their reasons and Must/Should/Later marks, and the "validate first" step; the parts become the starting rows of the Requirements table.
- If `reviews.csv` is available, re-read the cited reviews in full; look for details the report compressed (exact steps users found painful, edge cases, the words they use).
- If there's no report, ask for the problem in one question, or offer to run `mine-competitor-reviews` first. Don't invent evidence.

Also gather the user's own app context: platforms, stack, existing flows the feature touches, pricing model. Check conversation and memory before asking.

## 2. Decide scope before writing

Write the smallest version that resolves the complaint for most of the reviewers who raised it. Name explicitly what the reviews asked for that this version leaves out, and why. Prefer a scope the user can ship and validate in one or two weeks; put the rest in a later phase.

If the opportunity collides with one of the user's existing decisions (a pricing choice, an auto-delete, a fixed schedule), resolve it in the spec rather than leaving it implicit.

## 3. Write the spec

Publish it as a shareable document (Docs artifact type or docs connector when available, else an HTML artifact, else markdown), in the language of the user's request. Structure:

```
# <Feature name> — spec
## Why (2–3 sentences: the problem, its numbers and confidence label, which competitors fail at it; cite review ids)
## Goal and non-goals
## Users and moment of use (who, and the exact moment in their routine — e.g. "right after finishing a practice test")
## Flow (numbered steps of what the user sees and does; a diagram if it branches)
## Requirements (table: requirement, why — linked to review ids, priority Must/Should/Later)
## Edge cases (empty, offline, many items, failure mid-flow, undo)
## Acceptance criteria (testable statements, Given/When/Then or checklist)
## Success metrics (one primary metric tied to the complaint — e.g. time to add 5 items — plus a guardrail; target and how it's measured)
## Validation before full build (the cheapest experiment, what result means go / no-go)
## Store and launch line (the one sentence that tells competitors' unhappy users this is fixed)
## Open questions
```

Open the spec with a two-line **In short** under the title: what will be built, and the one thing that decides whether it worked. Give an overall effort estimate using the same scale as the report (S = 1–2 days, M = about a week, L = two weeks or more, for one developer). If the source problem's confidence is Weak, say so in Why and make the validation step a gate before the build, not a nice-to-have. Use plain words; when a term like "guardrail metric" is needed, explain it in a clause the first time.

Keep it short: most sections are a few lines or a small table. Engineering notes (data model changes, API calls, libraries) go under Requirements or Edge cases only when they affect scope or effort; add them in the user's own stack when known.

## 4. Check before handing off

- Every number and review id matches the report or CSV.
- Every Must requirement traces to evidence or to a stated product decision.
- Acceptance criteria are testable by someone who didn't write the spec.
- The primary metric would actually move if the complaint were solved.

## Finishing

In chat: one line on the scope you chose and the primary metric, then point to the spec. Offer one next step — breaking it into tasks, a UI mockup of the flow, or setting up the validation experiment.
