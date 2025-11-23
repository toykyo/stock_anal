from collections.abc import Sequence

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.api.deps import get_session
from app.models.keyword import Keyword
from app.models.keyword_stat import KeywordStat
from app.schemas.keyword import KeywordCreate, KeywordRead, KeywordStatRead

router = APIRouter()


@router.get("/", response_model=Sequence[KeywordRead])
def list_keywords(db: Session = Depends(get_session)):
    return db.scalars(select(Keyword)).all()


@router.post("/", response_model=KeywordRead)
def create_keyword(payload: KeywordCreate, db: Session = Depends(get_session)):
    keyword = Keyword(**payload.model_dump())
    db.add(keyword)
    db.commit()
    db.refresh(keyword)
    return keyword


@router.get("/{keyword_id}/stats", response_model=Sequence[KeywordStatRead])
def get_keyword_stats(keyword_id: int, db: Session = Depends(get_session)):
    stmt = select(KeywordStat).where(KeywordStat.keyword_id == keyword_id)
    return db.scalars(stmt).all()
