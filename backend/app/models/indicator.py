from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base_class import Base

if TYPE_CHECKING:  # pragma: no cover
    from app.models.indicator_link import IndicatorLink
    from app.models.indicator_value import IndicatorValue


class Indicator(Base):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    code: Mapped[str] = mapped_column(String(40), unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    description: Mapped[str | None] = mapped_column(String(255))
    frequency: Mapped[str | None] = mapped_column(String(40))
    unit: Mapped[str | None] = mapped_column(String(20))

    values: Mapped[list["IndicatorValue"]] = relationship(
        back_populates="indicator",
        cascade="all, delete-orphan",
    )
    links: Mapped[list["IndicatorLink"]] = relationship(
        back_populates="indicator",
        cascade="all, delete-orphan",
    )
