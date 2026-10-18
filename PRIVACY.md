# Privacy Policy

_Last updated: 18 October 2026_

One Star Gold is a plugin for Claude made of instructions and a small local script. It has no servers, accounts, analytics or telemetry. The author receives no data from your use of it.

## What the plugin reads

- **Public app store pages** (Google Play and, when you choose, the App Store) for the competitors you analyze. Reviews on these pages are written by members of the public and may show the reviewer's display name. The collection script keeps only the rating, date and review text; it does not record reviewer names.
- **Files you choose to give it**: iPhone screenshots of reviews or a review-tool CSV export.
- **Context you provide** about your own app, used only to tailor the report.

## What it creates

- A report and a `reviews.csv` table, saved in your own Claude workspace or document. They stay under your control; you can delete them at any time.

## What it sends elsewhere

- **Nothing by default.**
- **Apify (optional):** only if you have connected Apify to Claude yourself and approve a run. The plugin then sends competitor app identifiers and run settings (countries, number of reviews) to Apify to fetch public reviews. It never sends your personal data or credentials. Apify's handling of that request is covered by [Apify's privacy policy](https://apify.com/privacy-policy).

Claude itself processes everything under Anthropic's terms and privacy policy.

## What it never does

- Sign in to any store or account, post, rate or report.
- Work around a site or tool that refuses access.
- Collect information about children; the plugin is intended for adults building apps.

## Contact

Questions or requests: open an [issue](https://github.com/sude-go/one-star-gold/issues) or contact the author through [github.com/sude-go](https://github.com/sude-go).
