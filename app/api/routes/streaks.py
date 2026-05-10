from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.services.streak_service import (
    update_streak
)

router = APIRouter()


@router.post("/update")
async def streak_update(
    user_id: int,
    db: Session = Depends(get_db)
):
    return update_streak(
        db=db,
        user_id=user_id
    )