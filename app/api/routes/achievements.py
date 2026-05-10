from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.services.achievement_service import (
    get_user_achievements
)

from app.services.achievement_service import (
    unlock_achievement
)

router = APIRouter()


@router.post("/unlock")
async def achievement_unlock(
    user_id: int,
    achievement_id: int,
    db: Session = Depends(get_db)
):
    return unlock_achievement(
        db=db,
        user_id=user_id,
        achievement_id=achievement_id,
    )


@router.get("/{user_id}")
async def achievements(
    user_id: int,
    db: Session = Depends(get_db)
):
    return get_user_achievements(
        db=db,
        user_id=user_id
    )