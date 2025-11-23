from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class SectorBase(BaseModel):
    name: str = Field(..., max_length=100)
    description: Optional[str] = Field(default=None, max_length=255)
    market: Optional[str] = Field(default=None, max_length=32)
    slug: Optional[str] = Field(default=None, max_length=60)


class SectorCreate(SectorBase):
    pass


class SectorRead(SectorBase):
    id: int

    class Config:
        from_attributes = True
