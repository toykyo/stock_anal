from datetime import date
from typing import Iterable

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.daily_price import DailyPrice


def bulk_upsert_prices(db: Session, records: Iterable[dict]) -> int:
    count = 0
    for record in records:
        stmt = select(DailyPrice).where(
            DailyPrice.symbol_id == record["symbol_id"],
            DailyPrice.trade_date == record["trade_date"],
        )
        entity = db.execute(stmt).scalars().one_or_none()
        if entity:
            for key, value in record.items():
                setattr(entity, key, value)
        else:
            db.add(DailyPrice(**record))
        count += 1
    db.commit()
    return count
