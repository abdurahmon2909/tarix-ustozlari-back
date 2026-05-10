from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.services.daily_challenge_service import (
    get_today_challenge
)

router = APIRouter()


@router.get("/")
async def today_challenge(
    db: Session = Depends(get_db)
):
    return get_today_challenge(
        db=db
    )