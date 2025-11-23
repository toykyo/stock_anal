from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base_class import Base

if TYPE_CHECKING:  # pragma: no cover
    from app.models.indicator import Indicator
    from app.models.sector import Sector
    from app.models.symbol import Symbol


class IndicatorLink(Base):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    indicator_id: Mapped[int] = mapped_column(ForeignKey("indicator.id"), nullable=False)
    sector_id: Mapped[int | None] = mapped_column(ForeignKey("sector.id"))
    symbol_id: Mapped[int | None] = mapped_column(ForeignKey("symbol.id"))
    weight: Mapped[float | None] = mapped_column(Float)
    notes: Mapped[str | None]

    indicator: Mapped["Indicator"] = relationship(back_populates="links")
    sector: Mapped["Sector | None"] = relationship(back_populates="indicator_links")
    symbol: Mapped["Symbol | None"] = relationship(back_populates="indicator_links")
