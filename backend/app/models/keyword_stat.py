from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy import Date, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base_class import Base

if TYPE_CHECKING:  # pragma: no cover
    from app.models.keyword import Keyword


class KeywordStat(Base):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    keyword_id: Mapped[int] = mapped_column(ForeignKey("keyword.id"), nullable=False)
    stat_date: Mapped[date] = mapped_column(Date, nullable=False)
    search_volume: Mapped[float | None] = mapped_column(Float)
    sentiment: Mapped[float | None] = mapped_column(Float)
    delta_vs_prev: Mapped[float | None] = mapped_column(Float)

    keyword: Mapped["Keyword"] = relationship(back_populates="stats")
