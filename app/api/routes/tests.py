from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.models.question import Question

from app.schemas.question import QuestionResponse

from app.schemas.test_session import TestSessionCreate
from app.schemas.test_session import TestSessionResponse

from app.services.test_service import get_random_questions
from app.services.test_service import save_test_result

router = APIRouter()


@router.get(
    "/",
    response_model=list[QuestionResponse]
)
async def get_tests(
    db: Session = Depends(get_db)
):
    questions = db.query(
        Question
    ).all()

    return questions


@router.get(
    "/random",
    response_model=list[QuestionResponse]
)
async def random_tests(
    limit: int = 10,
    db: Session = Depends(get_db)
):
    return get_random_questions(
        db=db,
        limit=limit
    )


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


@router.post(
    "/submit",
    response_model=TestSessionResponse
)
async def submit_test(
    payload: TestSessionCreate,
    db: Session = Depends(get_db)
):
    return save_test_result(
        db=db,
        payload=payload
    )