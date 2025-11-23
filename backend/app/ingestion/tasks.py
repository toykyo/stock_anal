from datetime import datetime

from sqlalchemy.orm import Session

from app.models.ingestion_run import IngestionRun


def log_start(db: Session, job_name: str) -> IngestionRun:
    run = IngestionRun(job_name=job_name, started_at=datetime.utcnow(), status="running")
    db.add(run)
    db.commit()
    db.refresh(run)
    return run


def log_end(db: Session, run: IngestionRun, status: str, rows: int | None = None) -> None:
    run.finished_at = datetime.utcnow()
    run.status = status
    run.rows_processed = rows
    db.add(run)
    db.commit()
