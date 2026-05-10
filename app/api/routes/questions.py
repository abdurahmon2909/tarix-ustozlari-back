from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.models.question import Question

from app.schemas.question import (
    QuestionResponse
)

router = APIRouter()


@router.get(
    "/{question_id}",
    response_model=QuestionResponse
)
async def get_question(
    question_id: int,
    db: Session = Depends(get_db)
):
    question = db.query(
        Question
    ).filter(
        Question.id == question_id
    ).first()

    if not question:
        raise HTTPException(
            status_code=404,
            detail="Question not found"
        )

    return question