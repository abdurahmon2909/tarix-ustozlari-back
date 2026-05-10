from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import (
    get_db
)

from app.schemas.leaderboard import (
    LeaderboardUserResponse
)

from app.services.leaderboard_service import (
    get_leaderboard_service
)

router = APIRouter()


@router.get(
    "",
    response_model=list[
        LeaderboardUserResponse
    ]
)
async def leaderboard(
    db: Session = Depends(get_db)
):
    return get_leaderboard_service(
        db=db
    )