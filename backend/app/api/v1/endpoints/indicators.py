from collections.abc import Sequence

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app import schemas
from app.api.deps import get_session
from app.models.indicator import Indicator
from app.models.indicator_value import IndicatorValue

router = APIRouter()


@router.get("/", response_model=Sequence[schemas.IndicatorRead])
def list_indicators(db: Session = Depends(get_session)):
    return db.query(Indicator).all()


@router.post(
    "/", response_model=schemas.IndicatorRead, status_code=status.HTTP_201_CREATED
)
def create_indicator(
    payload: schemas.IndicatorCreate, db: Session = Depends(get_session)
):
    indicator = Indicator(**payload.model_dump())
    db.add(indicator)
    db.commit()
    db.refresh(indicator)
    return indicator


@router.get("/{indicator_id}", response_model=schemas.IndicatorRead)
def get_indicator(indicator_id: int, db: Session = Depends(get_session)):
    indicator = db.get(Indicator, indicator_id)
    if not indicator:
        raise HTTPException(status_code=404, detail="Indicator not found")
    return indicator


@router.get(
    "/{indicator_id}/values", response_model=Sequence[schemas.IndicatorValueRead]
)
def get_indicator_values(indicator_id: int, db: Session = Depends(get_session)):
    stmt = (
        select(IndicatorValue)
        .where(IndicatorValue.indicator_id == indicator_id)
        .order_by(IndicatorValue.effective_from.desc())
    )
    values = db.execute(stmt).scalars().all()
    if not values:
        indicator = db.get(Indicator, indicator_id)
        if not indicator:
            raise HTTPException(status_code=404, detail="Indicator not found")
    return values
