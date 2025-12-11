# Stock Analytics (Local, No Docker)

## 요구사항 대응 현황 (1,2)
- 업종/종목: sectors, symbols 테이블 및 CRUD API
- 일일 데이터: daily_prices 테이블 (종가, 종가증감, 거래량, 거래량증감, 외국인/기관/개인 순매수)
- upsert 로직: 동일 symbol_id+trade_date 입력 시 업데이트
- 델타 계산: `src/ingest.py` 의 `compute_deltas`, `ingest_daily`

## 파일
- `src/db.py` : MariaDB 연결, Base, SessionLocal
- `src/models.py` : SQLAlchemy 모델 (sectors, symbols, daily_prices)
- `src/main.py` : FastAPI 엔드포인트 (sectors/symbols/prices)
- `src/ingest.py` : 델타 계산 및 bulk upsert 예제

## MariaDB 스키마 (이미 코드에 반영)
- sectors(id, name, market, description, slug)
- symbols(id, ticker, name, market, isin, currency, sector_id FK)
- daily_prices(id, symbol_id FK, trade_date, close, close_delta, volume, volume_delta, foreign_net, institutional_net, individual_net), UNIQUE(symbol_id, trade_date)

## 실행 방법 (로컬 MariaDB)
1) MariaDB에 데이터베이스 생성:
   ```sql
   CREATE DATABASE stock_analytics CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
   ```
   계정/비밀번호에 맞게 `src/db.py` 의 `DATABASE_URL` 수정 (예: `mysql+pymysql://user:pass@localhost:3306/stock_analytics`).
2) 의존성 설치:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   pip install fastapi uvicorn sqlalchemy pymysql
   ```
3) API 실행:
   ```bash
   uvicorn src.main:app --reload
   ```
   Swagger: http://localhost:8000/docs
4) 사용 예시:
   - `POST /sectors` 로 섹터 등록
   - `POST /symbols` 로 종목 등록
   - `POST /prices` 로 일일 데이터 upsert (symbol_id+trade_date 고유)
   - `GET /prices?symbol_id=1` 로 조회
5) 델타 계산 + 적재 예제:
   ```bash
   python -m src.ingest
   ```
   (코드 내 sample_rows 참고; 실제로는 외부 API 데이터로 교체)

## 다음 단계
- Alembic 마이그레이션 추가
- 경제지표/환율 테이블 및 API 확장 (요구 3), 영향도/모델링 로직 (요구 4)
