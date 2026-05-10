from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.services.open_answer_service import (
    get_open_answer_questions
)

router = APIRouter()


@router.get("/")
async def open_answer_questions(
    db: Session = Depends(get_db)
):
    return get_open_answer_questions(
        db=db
    )