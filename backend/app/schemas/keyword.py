from datetime import date
from typing import Optional

from pydantic import BaseModel, Field


class KeywordBase(BaseModel):
    keyword: str = Field(..., max_length=80)
    category: Optional[str] = Field(default=None, max_length=40)


class KeywordCreate(KeywordBase):
    pass


class KeywordRead(KeywordBase):
    id: int

    class Config:
        from_attributes = True


class KeywordStatRead(BaseModel):
    id: int
    keyword_id: int
    stat_date: date
    search_volume: Optional[float] = None
    sentiment: Optional[float] = None
    delta_vs_prev: Optional[float] = None

    class Config:
        from_attributes = True
