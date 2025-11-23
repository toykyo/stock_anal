# Stock Analytics Platform

FastAPI + MariaDB + React monorepo that ingests KOSPI/KOSDAQ market data, macro indicators, and keyword trends. The goal is to store sector/symbol-level timelines, overlay macro indicators, and later build predictive models.

## Repository Structure

```
stock_anal/
├── backend/        # FastAPI app, SQLAlchemy models, ETL placeholders
├── frontend/       # React (Vite) dashboard
├── docker-compose.yml
└── README.md
```

## Quick Start

1. Copy `backend/.env.example` to `backend/.env` and adjust the MariaDB credentials.
2. Launch the stack:

```bash
docker compose up --build
```

Backend: http://localhost:8000/docs  
Frontend: http://localhost:5173  
MariaDB: localhost:3306 (user/pass `stock`/`stock`)

## Backend Highlights

- FastAPI w/ versioned routers under `app/api/v1`.
- SQLAlchemy models capture: sectors, symbols, daily prices, indicators, indicator links, keyword stats, ingestion runs.
- Services layer provides reusable upsert helpers for ETL jobs.
- Pydantic Settings loads configuration from `.env`.
- Future ETL jobs land in `app/ingestion`, ready for APScheduler/Celery integration.

## Frontend Highlights

- Vite + React + React Query for data fetching.
- Routing scaffold for sector overview, symbol detail, indicator dashboard, and keyword placeholder.
- Axios API client reading from `VITE_API_URL` (defaults to `/api/v1` when proxied).

## Next Steps

- Implement concrete ingestion pipelines (KRX, macro APIs, keyword feeds) that populate the MariaDB schema.
- Add Alembic migrations + seed scripts.
- Connect indicators to sectors/symbols with derived weights/correlations.
- Extend the frontend with real charts (e.g., Recharts/ECharts) and filtering.
