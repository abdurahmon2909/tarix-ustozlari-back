from fastapi import APIRouter

from app.schemas.daily import (
    DailyChallengeResponse
)

from app.services.daily_service import (
    get_daily_challenge_service
)

router = APIRouter()


@router.get(
    "",
    response_model=
    DailyChallengeResponse
)
async def daily_challenge():
    return get_daily_challenge_service()