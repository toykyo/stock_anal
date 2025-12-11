from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select
from src.db import Base, engine, get_db
from src.models import Sector, Symbol, DailyPrice

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Stock Analytics API")

@app.post("/sectors", status_code=status.HTTP_201_CREATED)
def create_sector(payload: dict, db: Session = Depends(get_db)):
    sector = Sector(**payload)
    db.add(sector)
    db.commit()
    db.refresh(sector)
    return sector

@app.get("/sectors")
def list_sectors(db: Session = Depends(get_db)):
    return db.execute(select(Sector)).scalars().all()

@app.post("/symbols", status_code=status.HTTP_201_CREATED)
def create_symbol(payload: dict, db: Session = Depends(get_db)):
    symbol = Symbol(**payload)
    db.add(symbol)
    db.commit()
    db.refresh(symbol)
    return symbol

@app.get("/symbols")
def list_symbols(db: Session = Depends(get_db)):
    return db.execute(select(Symbol)).scalars().all()

@app.post("/prices", status_code=status.HTTP_201_CREATED)
def upsert_price(payload: dict, db: Session = Depends(get_db)):
    stmt = select(DailyPrice).where(
        DailyPrice.symbol_id == payload["symbol_id"],
        DailyPrice.trade_date == payload["trade_date"],
    )
    existing = db.execute(stmt).scalars().one_or_none()
    if existing:
        for k, v in payload.items():
            setattr(existing, k, v)
        entity = existing
    else:
        entity = DailyPrice(**payload)
        db.add(entity)
    db.commit()
    db.refresh(entity)
    return entity

@app.get("/prices")
def list_prices(symbol_id: int | None = None, db: Session = Depends(get_db)):
    stmt = select(DailyPrice)
    if symbol_id:
        stmt = stmt.where(DailyPrice.symbol_id == symbol_id)
    stmt = stmt.order_by(DailyPrice.trade_date.desc()).limit(500)
    return db.execute(stmt).scalars().all()
