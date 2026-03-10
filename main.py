from fastapi import FastAPI
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded

from app.core.config import settings
from app.middleware.security import limiter
from app.api import market_routes

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Register Rate Limiter
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# Include Routers
app.include_router(market_routes.router, prefix=settings.API_V1_STR, tags=["Market Analysis"])

@app.get("/")
def root():
    return {"message": "Trade Opportunities API is running. Access docs at /docs"}
