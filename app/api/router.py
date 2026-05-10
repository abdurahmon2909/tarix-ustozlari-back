from fastapi import APIRouter

from app.api.v1.endpoints import (
    auth,
    home,
    tests,
    books,
    statistics,
    users,
    leaderboard,
    search,
    ai,
    daily,
    seed
)

api_router = APIRouter()

api_router.include_router(
    auth.router,
    prefix="/auth",
    tags=["Auth"]
)

api_router.include_router(
    home.router,
    prefix="/home",
    tags=["Home"]
)

api_router.include_router(
    tests.router,
    prefix="/tests",
    tags=["Tests"]
)

api_router.include_router(
    books.router,
    prefix="/books",
    tags=["Books"]
)

api_router.include_router(
    statistics.router,
    prefix="/statistics",
    tags=["Statistics"]
)

api_router.include_router(
    users.router,
    prefix="/users",
    tags=["Users"]
)

api_router.include_router(
    leaderboard.router,
    prefix="/leaderboard",
    tags=["Leaderboard"]
)

api_router.include_router(
    search.router,
    prefix="/search",
    tags=["Search"]
)

api_router.include_router(
    ai.router,
    prefix="/ai",
    tags=["AI"]
)

api_router.include_router(
    daily.router,
    prefix="/daily-challenges",
    tags=["Daily"]
)