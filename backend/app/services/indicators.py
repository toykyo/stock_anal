from sqlalchemy.orm import Session

from app.models.indicator import Indicator


def upsert_indicator(db: Session, data: dict) -> Indicator:
    indicator = (
        db.query(Indicator).filter(Indicator.code == data["code"]).one_or_none()
    )
    if indicator:
        for key, value in data.items():
            setattr(indicator, key, value)
    else:
        indicator = Indicator(**data)
        db.add(indicator)
    db.commit()
    db.refresh(indicator)
    return indicator

