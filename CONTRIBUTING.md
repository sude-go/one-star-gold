# Contributing to One Star Gold

Thanks for helping make competitor review analysis more honest and more useful.

## Reporting a problem

Open an [issue](https://github.com/sude-go/one-star-gold/issues/new/choose) and include:

- the plugin version (`claude plugin list` shows it),
- where you ran it (Claude Code terminal, desktop app, claude.ai / Cowork) and which browser tool was available,
- the app category, store and country you analyzed,
- what went wrong: a wrong number, a missed competitor, a collection step that failed, a report section that was confusing.

Please don't paste full review dumps or anything personal; a few review ids from the CSV are enough.

## Suggesting a change

Ideas are welcome as issues first, so we can agree on the shape before code. Good candidates: new review sources, store page changes that break collection, clearer report wording, more languages for the Google Play extraction script.

## Making a change

1. Fork the repository and create a branch.
2. Keep skill instructions in `skills/*/SKILL.md` short and explain *why* a rule exists; put long mechanics in `references/`.
3. If you touch `scripts/count_themes.py`, run it on a sample CSV and include the output in the pull request.
4. Validate before opening the pull request:

   ```bash
   claude plugin validate --strict .
   ```

5. Bump `version` in `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json`, and add a line to `CHANGELOG.md`.

## Ground rules for the plugin's behavior

- Public pages only; never sign in, post, rate or report on a store.
- Never work around a site or tool that refuses access.
- Anything that costs the user money (e.g. Apify) runs only after they approve the cost.
- Every number in a report must come from the counting script, and every claim must cite review ids.
