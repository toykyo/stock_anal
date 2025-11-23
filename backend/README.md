# Backend (FastAPI)

## Local Development

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate  # Linux/macOS: source .venv/bin/activate
pip install -e .
uvicorn app.main:app --reload
```

Copy `.env.example` to `.env` and adjust the MariaDB URL before running the API.

## Folder Layout

- `app/core` – configuration, logging helpers.
- `app/db` – SQLAlchemy engine/session helpers and model registry.
- `app/models` – ORM models for sectors, symbols, indicators, etc.
- `app/schemas` – Pydantic schemas mirroring the models.
- `app/api` – FastAPI routers, dependencies, and versioned endpoints.
- `app/services` – business/domain logic per bounded context.
- `app/ingestion` – task definitions for historical + daily ETL.

Alembic migrations can be added later under `alembic/` once the schema is finalized.
