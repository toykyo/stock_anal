from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base_class import Base

if TYPE_CHECKING:  # pragma: no cover
    from app.models.keyword_stat import KeywordStat


class Keyword(Base):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    keyword: Mapped[str] = mapped_column(String(80), unique=True, nullable=False)
    category: Mapped[str | None] = mapped_column(String(40))

    stats: Mapped[list["KeywordStat"]] = relationship(
        back_populates="keyword",
        cascade="all, delete-orphan",
    )
