from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base_class import Base

if TYPE_CHECKING:  # pragma: no cover
    from app.models.indicator_link import IndicatorLink
    from app.models.symbol import Symbol


class Sector(Base):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    description: Mapped[str | None] = mapped_column(String(255))
    market: Mapped[str | None] = mapped_column(String(32))
    slug: Mapped[str | None] = mapped_column(String(60), unique=True)

    symbols: Mapped[list["Symbol"]] = relationship(
        back_populates="sector", cascade="all, delete-orphan"
    )
    indicator_links: Mapped[list["IndicatorLink"]] = relationship(
        back_populates="sector",
        cascade="all, delete-orphan",
    )
