# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

NewsDigest is a Python application that fetches news from NewsAPI based on user-defined topics, summarizes them using Anthropic's API, and delivers digests via email. It uses FastAPI for its web layer. The project is in early development — only the config loader and news API client are implemented; most service modules are scaffolded but empty.

## Commands

```bash
# Activate virtual environment (Windows)
./venv/Scripts/activate

# Install dependencies (note the typo in filename)
pip install -r requeriments.txt

# Run the test script
python test.py

# Run tests with pytest
pytest
```

No build step, linter, or CI pipeline is configured yet.

## Architecture

```
config/settings.py      → Loads .env credentials (NEWS_APIKEY, ANTHROPIC_APIKEY, EMAIL_SENDER)
api/news_client.py      → Fetches articles from NewsAPI.org (/v2/everything)
services/processor.py   → (stub) News processing pipeline
services/summarizer.py  → (stub) AI summarization via Anthropic
services/mailer.py      → (stub) Email delivery
db/database.py          → (stub) Data persistence
models/user.py          → (stub) User model / subscriptions
main.py                 → (stub) Application entry point, intended for FastAPI
scheduler.py            → (stub) Periodic task orchestration
```

**Data flow:** Config → NewsAPI fetch → Process → Summarize → Email

## Key Details

- Python 3.11.3 with virtualenv at `venv/`
- Environment variables loaded from `.env` via `python-dotenv`
- `news_client.fetch_news(topics, language='es', country='mx')` defaults to Spanish/Mexico
- Core dependencies: FastAPI, Requests, BeautifulSoup4, Pydantic, python-dotenv
- The requirements file (`requeriments.txt`) contains many ML/CV libraries not currently used by the project
