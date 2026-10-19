# Gamba leaderboard

A single responsive page with a **View leaderboard** link to:

https://gamba.com/promotions/exclusive-leaderboards/25084

No API, build step, JavaScript dependencies, or data configuration is required.

## Local preview

```sh
npm run dev
```

Open `http://127.0.0.1:5173` or `http://127.0.0.1:5173/gamba`.

## Files

- `dist/index.html` — page content and podium illustration
- `dist/styles.css` — responsive styles
- `dist/assets/` — self-hosted fonts and favicon

The page is served at both `/` and `/gamba`. All leaderboard links open the supplied Gamba URL in a new tab.

## Vercel

Import this repository with the repository root as the Root Directory. The committed `vercel.json` configures a static site, skips installation and building, and publishes `dist/` as the site root. Pushes to `main` trigger Vercel's connected Git deployment.
