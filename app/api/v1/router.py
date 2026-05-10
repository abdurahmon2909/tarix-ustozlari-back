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
    seed,
    arena,
    notifications
)

api_router = APIRouter()

# AUTH
api_router.include_router(
    auth.router,
    prefix="/auth",
    tags=["Auth"]
)

# HOME
api_router.include_router(
    home.router,
    prefix="/home",
    tags=["Home"]
)

# TESTS
api_router.include_router(
    tests.router,
    prefix="/tests",
    tags=["Tests"]
)

# BOOKS
api_router.include_router(
    books.router,
    prefix="/books",
    tags=["Books"]
)

# USERS
api_router.include_router(
    users.router,
    prefix="/users",
    tags=["Users"]
)

# STATISTICS
api_router.include_router(
    statistics.router,
    prefix="/statistics",
    tags=["Statistics"]
)

# LEADERBOARD
api_router.include_router(
    leaderboard.router,
    prefix="/leaderboard",
    tags=["Leaderboard"]
)

# SEARCH
api_router.include_router(
    search.router,
    prefix="/search",
    tags=["Search"]
)

# AI
api_router.include_router(
    ai.router,
    prefix="/ai",
    tags=["AI"]
)

# DAILY CHALLENGES
api_router.include_router(
    daily.router,
    prefix="/daily-challenges",
    tags=["Daily"]
)

# SEED
api_router.include_router(
    seed.router,
    prefix="/seed",
    tags=["Seed"]
)

# ADMIN
api_router.include_router(
    admin.router,
    prefix="/admin",
    tags=["Admin"]
)
api_router.include_router(
    arena.router,
    prefix="/arena",
    tags=["Arena"]
)
api_router.include_router(
    notifications.router,
    prefix="/notifications",
    tags=["Notifications"]
)