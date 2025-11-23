from datetime import date
from typing import Optional

from pydantic import BaseModel


class DailyPriceBase(BaseModel):
    trade_date: date
    close: float
    close_delta: Optional[float] = None
    volume: Optional[int] = None
    volume_delta: Optional[int] = None
    foreign_net: Optional[float] = None
    institutional_net: Optional[float] = None
    individual_net: Optional[float] = None


class DailyPriceCreate(DailyPriceBase):
    symbol_id: int


class DailyPriceRead(DailyPriceBase):
    id: int
    symbol_id: int

    class Config:
        from_attributes = True
