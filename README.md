# Trapsoul Researcher

Professional research and ideation workspace for **Hip Hop, R&B, Trap Soul and adjacent urban music**.

> Research first. Generate second. Verify before publishing.

## Features
- Trend discovery by market (USA/global/country)
- Keyword research with optional Google Ads Keyword Planner
- YouTube metadata research via official YouTube Data API
- Spotify catalog lookup via official Web API
- Topic/keyword analysis and opportunity signals
- Original song-title ideation
- Original lyric concepts and song structures
- YouTube/Spotify/TikTok/Instagram SEO metadata
- Evidence, timestamps and confidence labels
- SQLite cache foundation
- REST API + dashboard
- CLI, Docker and GitHub Actions

## Architecture
```
UI / CLI -> FastAPI -> Research Orchestrator
                    -> YouTube / Spotify / Google Trends / Google Ads
                    -> Analytics
                    -> Creative Engine
                    -> SQLite
```

## Quick start
```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -e '.[dev]'
cp .env.example .env
uvicorn app.main:app --reload
```
Open http://127.0.0.1:8000 and /docs.

## Provider notes
Spotify's 2026 Developer Mode has tighter limits and removed/restricted several recommendation/audio-analysis features for new apps, so this project uses Spotify for catalog lookup rather than making the product dependent on those endpoints.
Google Ads Keyword Planning provides keyword ideas and historical metrics, but is quota/rate limited and should be cached.
Google Trends has no generally available official public API for this use case; the optional pytrends adapter is explicitly best-effort.

## Copyright
The project does not scrape or reproduce copyrighted lyrics. Creative output is original concepts, prompts and metadata. Trend claims must come from observed provider data.

## Environment
See .env.example. Never commit real credentials.
