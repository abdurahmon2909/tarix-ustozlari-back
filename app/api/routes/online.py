from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.services.online_service import (
    set_online
)

from app.services.online_service import (
    set_offline
)

router = APIRouter()


@router.post("/online")
async def online(
    user_id: int,
    db: Session = Depends(get_db)
):
    return set_online(
        db=db,
        user_id=user_id
    )


@router.post("/offline")
async def offline(
    user_id: int,
    db: Session = Depends(get_db)
):
    return set_offline(
        db=db,
        user_id=user_id
    )