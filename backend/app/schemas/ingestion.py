from datetime import datetime

from pydantic import BaseModel, Field


class IngestionRunRead(BaseModel):
    id: int
    job_name: str
    started_at: datetime
    finished_at: datetime | None = None
    status: str = Field(..., max_length=20)
    rows_processed: int | None = None

    class Config:
        from_attributes = True
