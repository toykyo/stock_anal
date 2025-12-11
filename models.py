from datetime import datetime, date
from sqlalchemy import String, Integer, BigInteger, Date, DateTime, DECIMAL, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .db import Base

class Sector(Base):
    __tablename__ = "sectors"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    market: Mapped[str | None] = mapped_column(String(32))
    description: Mapped[str | None] = mapped_column(String(255))
    slug: Mapped[str | None] = mapped_column(String(60), unique=True)
    symbols = relationship("Symbol", back_populates="sector", cascade="all, delete-orphan")

class Symbol(Base):
    __tablename__ = "symbols"
    __table_args__ = (
        UniqueConstraint("ticker", name="uq_symbol_ticker"),
        UniqueConstraint("isin", name="uq_symbol_isin"),
    )
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    ticker: Mapped[str] = mapped_column(String(20), nullable=False)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    market: Mapped[str | None] = mapped_column(String(20))
    isin: Mapped[str | None] = mapped_column(String(40))
    currency: Mapped[str | None] = mapped_column(String(8), default="KRW")
    sector_id: Mapped[int | None] = mapped_column(ForeignKey("sectors.id"))
    listing_date: Mapped[datetime | None] = mapped_column(DateTime)
    sector = relationship("Sector", back_populates="symbols")
    prices = relationship("DailyPrice", back_populates="symbol", cascade="all, delete-orphan")

class DailyPrice(Base):
    __tablename__ = "daily_prices"
    __table_args__ = (UniqueConstraint("symbol_id", "trade_date", name="uq_price_symbol_date"),)
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    symbol_id: Mapped[int] = mapped_column(ForeignKey("symbols.id"), nullable=False)
    trade_date: Mapped[date] = mapped_column(Date, nullable=False)
    close: Mapped[float] = mapped_column(DECIMAL(18, 4), nullable=False)
    close_delta: Mapped[float | None] = mapped_column(DECIMAL(18, 4))
    volume: Mapped[int | None] = mapped_column(BigInteger)
    volume_delta: Mapped[int | None] = mapped_column(BigInteger)
    foreign_net: Mapped[float | None] = mapped_column(DECIMAL(18, 4))
    institutional_net: Mapped[float | None] = mapped_column(DECIMAL(18, 4))
    individual_net: Mapped[float | None] = mapped_column(DECIMAL(18, 4))
    symbol = relationship("Symbol", back_populates="prices")
