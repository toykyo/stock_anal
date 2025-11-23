from collections.abc import Sequence

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app import schemas
from app.api.deps import get_session
from app.models.daily_price import DailyPrice

router = APIRouter()


@router.get("/", response_model=Sequence[schemas.DailyPriceRead])
def list_prices(
    symbol_id: int | None = None,
    limit: int = Query(250, le=3650),
    db: Session = Depends(get_session),
):
    stmt = select(DailyPrice)
    if symbol_id:
        stmt = stmt.where(DailyPrice.symbol_id == symbol_id)
    stmt = stmt.order_by(DailyPrice.trade_date.desc()).limit(limit)
    return db.execute(stmt).scalars().all()


@router.post(
    "/", response_model=schemas.DailyPriceRead, status_code=status.HTTP_201_CREATED
)
def create_price(payload: schemas.DailyPriceCreate, db: Session = Depends(get_session)):
    entity = DailyPrice(**payload.model_dump())
    db.add(entity)
    db.commit()
    db.refresh(entity)
    return entity


@router.get("/{price_id}", response_model=schemas.DailyPriceRead)
def get_price(price_id: int, db: Session = Depends(get_session)):
    entity = db.get(DailyPrice, price_id)
    if not entity:
        raise HTTPException(status_code=404, detail="Price not found")
    return entity

