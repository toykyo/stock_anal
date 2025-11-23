from datetime import date
from typing import Optional

from pydantic import BaseModel, Field


class IndicatorBase(BaseModel):
    code: str = Field(..., max_length=40)
    name: str = Field(..., max_length=120)
    description: Optional[str] = Field(default=None, max_length=255)
    frequency: Optional[str] = Field(default=None, max_length=40)
    unit: Optional[str] = Field(default=None, max_length=20)


class IndicatorCreate(IndicatorBase):
    pass


class IndicatorRead(IndicatorBase):
    id: int

    class Config:
        from_attributes = True


class IndicatorValueRead(BaseModel):
    id: int
    indicator_id: int
    report_date: date
    effective_from: date
    value: float
    delta_vs_prev: Optional[float] = None
    payload: Optional[dict] = None

    class Config:
        from_attributes = True
