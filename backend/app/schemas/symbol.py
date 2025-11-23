from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class SymbolBase(BaseModel):
    ticker: str = Field(..., max_length=20)
    name: str = Field(..., max_length=120)
    market: Optional[str] = Field(default=None, max_length=20)
    isin: Optional[str] = Field(default=None, max_length=40)
    currency: Optional[str] = Field(default="KRW", max_length=8)
    sector_id: Optional[int] = None
    listing_date: Optional[datetime] = None


class SymbolCreate(SymbolBase):
    pass


class SymbolRead(SymbolBase):
    id: int

    class Config:
        from_attributes = True
