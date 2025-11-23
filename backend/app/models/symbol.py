from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base_class import Base

if TYPE_CHECKING:  # pragma: no cover
    from app.models.daily_price import DailyPrice
    from app.models.indicator_link import IndicatorLink
    from app.models.sector import Sector


class Symbol(Base):
    __table_args__ = (
        UniqueConstraint("ticker", name="uq_symbol_ticker"),
        UniqueConstraint("isin", name="uq_symbol_isin"),
    )

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    ticker: Mapped[str] = mapped_column(String(20), nullable=False)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    market: Mapped[str] = mapped_column(String(20))
    isin: Mapped[str | None] = mapped_column(String(40))
    currency: Mapped[str | None] = mapped_column(String(8), default="KRW")
    sector_id: Mapped[int | None] = mapped_column(ForeignKey("sector.id"))
    listing_date: Mapped[datetime | None] = mapped_column(DateTime)

    sector: Mapped["Sector | None"] = relationship(back_populates="symbols")
    prices: Mapped[list["DailyPrice"]] = relationship(
        back_populates="symbol",
        cascade="all, delete-orphan",
    )
    indicator_links: Mapped[list["IndicatorLink"]] = relationship(
        back_populates="symbol",
        cascade="all, delete-orphan",
    )
