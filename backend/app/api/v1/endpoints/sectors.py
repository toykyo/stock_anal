from collections.abc import Sequence

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import schemas
from app.api.deps import get_session
from app.models.sector import Sector

router = APIRouter()


@router.get("/", response_model=Sequence[schemas.SectorRead])
def list_sectors(db: Session = Depends(get_session)):
    return db.query(Sector).all()


@router.post(
    "/", response_model=schemas.SectorRead, status_code=status.HTTP_201_CREATED
)
def create_sector(payload: schemas.SectorCreate, db: Session = Depends(get_session)):
    sector = Sector(**payload.model_dump())
    db.add(sector)
    db.commit()
    db.refresh(sector)
    return sector


@router.get("/{sector_id}", response_model=schemas.SectorRead)
def get_sector(sector_id: int, db: Session = Depends(get_session)):
    sector = db.get(Sector, sector_id)
    if not sector:
        raise HTTPException(status_code=404, detail="Sector not found")
    return sector

