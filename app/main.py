from fastapi import FastAPI

from app.core.config import (
    settings
)

from app.core.version import (
    API_VERSION
)

from app.api.v1.router import (
    api_router
)

from app.core.exceptions import (
    AppException
)

from app.core.handlers import (
    app_exception_handler
)

from app.websockets.battle import (
    router as battle_ws_router
)

from app.core.rate_limit import (
    rate_limit_middleware
)

app = FastAPI(
    title=settings.PROJECT_NAME,

    version=API_VERSION
)

app.middleware("http")(
    rate_limit_middleware
)

app.add_exception_handler(
    AppException,
    app_exception_handler
)

app.include_router(
    api_router,
    prefix="/api/v1"
)

app.include_router(
    battle_ws_router
)


@app.get("/")
async def root():
    return {
        "message":
            "Tarix Backend API"
    }