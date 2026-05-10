from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.schemas.arena import ArenaMatchCreate
from app.schemas.arena import ArenaMatchResponse

from app.schemas.question import QuestionResponse

from app.services.arena_service import (
    create_arena_match
)

from app.services.arena_service import (
    generate_battle_questions
)

router = APIRouter()


@router.post(
    "/create",
    response_model=ArenaMatchResponse
)
async def create_match(
    payload: ArenaMatchCreate,
    db: Session = Depends(get_db)
):
    return create_arena_match(
        db=db,
        player_one_id=payload.player_one_id
    )


@router.get(
    "/questions",
    response_model=list[QuestionResponse]
)
async def battle_questions(
    limit: int = 10,
    db: Session = Depends(get_db)
):
    return generate_battle_questions(
        db=db,
        limit=limit
    )