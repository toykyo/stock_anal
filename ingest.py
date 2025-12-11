from datetime import date
from sqlalchemy import select
from sqlalchemy.orm import Session
from src.db import SessionLocal
from src.models import DailyPrice


def compute_deltas(rows: list[dict]) -> list[dict]:
    rows = sorted(rows, key=lambda r: r["trade_date"])
    prev = None
    for row in rows:
        if prev:
            row["close_delta"] = round(row["close"] - prev["close"], 4)
            if row.get("volume") is not None and prev.get("volume") is not None:
                row["volume_delta"] = row["volume"] - prev["volume"]
        prev = row
    return rows


def bulk_upsert(db: Session, records: list[dict]) -> int:
    count = 0
    for rec in records:
        stmt = select(DailyPrice).where(
            DailyPrice.symbol_id == rec["symbol_id"],
            DailyPrice.trade_date == rec["trade_date"],
        )
        existing = db.execute(stmt).scalars().one_or_none()
        if existing:
            for k, v in rec.items():
                setattr(existing, k, v)
        else:
            db.add(DailyPrice(**rec))
        count += 1
    db.commit()
    return count


def ingest_daily(raw_rows: list[dict]) -> int:
    rows = compute_deltas(raw_rows)
    with SessionLocal() as db:
        return bulk_upsert(db, rows)

if __name__ == "__main__":
    sample_rows = [
        {
            "symbol_id": 1,
            "trade_date": date(2024, 12, 1),
            "close": 10000,
            "volume": 120000,
            "foreign_net": 100,
            "institutional_net": -50,
            "individual_net": -50,
        },
        {
            "symbol_id": 1,
            "trade_date": date(2024, 12, 2),
            "close": 10200,
            "volume": 150000,
            "foreign_net": -20,
            "institutional_net": 10,
            "individual_net": 10,
        },
    ]
    inserted = ingest_daily(sample_rows)
    print(f"rows upserted: {inserted}")
