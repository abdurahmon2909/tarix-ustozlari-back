from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.services.quiz_room_service import (
    create_room
)

from app.services.quiz_room_service import (
    join_room
)

router = APIRouter()


@router.post("/create")
async def room_create(
    title: str,
    owner_user_id: int,
    max_players: int = 50,
    db: Session = Depends(get_db)
):
    return create_room(
        db=db,
        title=title,
        owner_user_id=owner_user_id,
        max_players=max_players,
    )


@router.post("/join")
async def room_join(
    room_code: str,
    user_id: int,
    db: Session = Depends(get_db)
):
    return join_room(
        db=db,
        room_code=room_code,
        user_id=user_id,
    )