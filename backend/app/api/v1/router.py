from fastapi import APIRouter

from app.api.v1.endpoints import (
    health,
    indicators,
    keywords,
    prices,
    sectors,
    symbols,
)

api_router = APIRouter()

api_router.include_router(health.router, prefix="/health", tags=["health"])
api_router.include_router(sectors.router, prefix="/sectors", tags=["sectors"])
api_router.include_router(symbols.router, prefix="/symbols", tags=["symbols"])
api_router.include_router(prices.router, prefix="/prices", tags=["prices"])
api_router.include_router(indicators.router, prefix="/indicators", tags=["indicators"])
api_router.include_router(keywords.router, prefix="/keywords", tags=["keywords"])
