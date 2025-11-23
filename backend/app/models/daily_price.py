from __future__ import annotations

from datetime import date, datetime
from typing import TYPE_CHECKING

from sqlalchemy import (
    Date,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    Numeric,
    UniqueConstraint,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base_class import Base

if TYPE_CHECKING:  # pragma: no cover
    from app.models.symbol import Symbol


class DailyPrice(Base):
    __table_args__ = (
        UniqueConstraint("symbol_id", "trade_date", name="uq_price_symbol_date"),
    )

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    symbol_id: Mapped[int] = mapped_column(ForeignKey("symbol.id"), nullable=False)
    trade_date: Mapped[date] = mapped_column(Date, nullable=False)
    close: Mapped[float] = mapped_column(Numeric(18, 4), nullable=False)
    close_delta: Mapped[float | None] = mapped_column(Numeric(18, 4))
    volume: Mapped[int | None] = mapped_column(Integer)
    volume_delta: Mapped[int | None] = mapped_column(Integer)
    foreign_net: Mapped[float | None] = mapped_column(Numeric(18, 4))
    institutional_net: Mapped[float | None] = mapped_column(Numeric(18, 4))
    individual_net: Mapped[float | None] = mapped_column(Numeric(18, 4))
    created_at: Mapped[datetime | None] = mapped_column(DateTime)

    symbol: Mapped["Symbol"] = relationship(back_populates="prices")
