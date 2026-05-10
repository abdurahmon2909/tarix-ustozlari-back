from fastapi import APIRouter

from app.services.matchmaking_service import (
    join_matchmaking
)

router = APIRouter()


@router.post("/find")
async def find_battle(
    user_id: int
):
    return join_matchmaking(
        user_id=user_id
    )