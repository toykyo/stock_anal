from collections.abc import Sequence

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import schemas
from app.api.deps import get_session
from app.models.symbol import Symbol

router = APIRouter()


@router.get("/", response_model=Sequence[schemas.SymbolRead])
def list_symbols(db: Session = Depends(get_session)):
    return db.query(Symbol).all()


@router.post("/", response_model=schemas.SymbolRead, status_code=status.HTTP_201_CREATED)
def create_symbol(payload: schemas.SymbolCreate, db: Session = Depends(get_session)):
    symbol = Symbol(**payload.model_dump())
    db.add(symbol)
    db.commit()
    db.refresh(symbol)
    return symbol


@router.get("/{symbol_id}", response_model=schemas.SymbolRead)
def get_symbol(symbol_id: int, db: Session = Depends(get_session)):
    symbol = db.get(Symbol, symbol_id)
    if not symbol:
        raise HTTPException(status_code=404, detail="Symbol not found")
    return symbol

