# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

NewsDigest fetches news from NewsAPI based on per-user topics stored in SQLite, summarizes each article via Anthropic's API, and delivers HTML digests via Gmail SMTP. A `schedule`-based scheduler runs the daily digest automatically at 06:00. A FastAPI REST API (`api.py`) is in development to allow user registration.

## Commands

```bash
# Activate virtual environment (Linux)
source venv/bin/activate

# Install dependencies (note the intentional typo in filename)
pip install -r requeriments.txt

# Initialize the SQLite database (run once before first use)
python -c "from db.database import init_db; init_db()"

# Run a single digest immediately
python -m main

# Run the scheduler (loops forever, fires at 06:00 daily)
python scheduler.py

# Run the FastAPI dev server
uvicorn rest_api:app --reload

# Ad-hoc test for the summarizer (hits live Anthropic API)
python -m test_db
```

> **Critical:** Always run from the project root using `python -m <module>`. Running files directly (e.g., `python services/summarizer.py`) will cause import errors.

## Architecture

```
config/settings.py    → Loads .env; raises ValueError if any credential is missing
api/news_client.py    → GET /v2/everything with OR-joined topics; returns {status, total_results, fetched_at, articles}
services/processor.py → Deduplicates articles per tag using Jaccard similarity (≥50% word overlap = duplicate)
services/summarizer.py → Calls Anthropic claude-sonnet-4-20250514 (max_tokens=150); falls back to article['description'] on error
services/mailer.py    → Gmail SMTP via smtplib; sends HTML email; EMAIL_PASSWORD must be a Gmail App Password
db/database.py        → SQLite (newsdigest.db created in project root); tables: users, user_tags
main.py               → send_daily_digest(): iterates all users → fetch by tag → deduplicate → summarize → email
scheduler.py          → Wraps send_daily_digest() with schedule.every().day.at("6:00")
rest_api.py           → FastAPI REST API (in development); POST /register validates UserRegister (Pydantic) and creates user+tags
models/user.py        → Currently empty; reserved for future User model
```

**Data flow:** DB (users + tags) → NewsAPI fetch per tag → Jaccard dedup → Anthropic summarize → Gmail send

## Key Details

- **`.env` variables required:** `NEWS_APIKEY`, `ANTHROPIC_APIKEY`, `EMAIL_SENDER`, `EMAIL_PASSWORD`
- `newsdigest.db` is created in the **project root** (wherever the process is launched), not inside any subdirectory
- `fetch_news(topics)` expects `topics` to be iterable (list/tuple); it joins them with ` OR `
- The multi-tag path in `send_daily_digest` picks only the first article per tag (`fetchNews[0]`); the single-tag path takes up to 5 (`fetchNews[0:5]`)
- `test_db.py` is actually a summarizer smoke test (misleading name) — it hits the live Anthropic API
- The venv uses Python 3.14; the requirements file (`requeriments.txt`) contains legacy ML/CV libs not used by the project
- `api.py` POST /register enforces 1–3 tags; returns 400 if email is already registered or tag count is invalid
