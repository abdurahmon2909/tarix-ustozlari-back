from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import (
    get_db
)

from app.schemas.test import (
    TestResponse,
    StartTestRequest,
    StartTestResponse,
    SessionQuestionsResponse,
    SubmitAnswerRequest,
    SubmitAnswerResponse,
    TestResultResponse
)

from app.services.test_service import (
    get_tests_service,
    get_session_questions_service
)

from app.services.test_engine_service import (
    start_test_service,
    submit_answer_service,
    finish_test_service
)

router = APIRouter()


@router.get(
    "",
    response_model=list[
        TestResponse
    ]
)
async def get_tests():
    return get_tests_service()


@router.post(
    "/start",
    response_model=
    StartTestResponse
)
async def start_test(
    payload: StartTestRequest,
    db: Session = Depends(get_db)
):
    return start_test_service(
        db=db,
        test_id=payload.test_id,
        user_id=payload.user_id
    )


@router.get(
    "/session/{session_id}",
    response_model=
    SessionQuestionsResponse
)
async def session_questions(
    session_id: int,
    db: Session = Depends(get_db)
):
    return get_session_questions_service(
        db=db,
        session_id=session_id
    )


@router.post(
    "/submit-answer",
    response_model=
    SubmitAnswerResponse
)
async def submit_answer(
    payload:
    SubmitAnswerRequest,
    db: Session = Depends(get_db)
):
    return submit_answer_service(
        db=db,
        session_id=
            payload.session_id,

        question_id=
            payload.question_id,

        selected_answer=
            payload.selected_answer
    )


@router.get(
    "/result/{session_id}",
    response_model=
    TestResultResponse
)
async def test_result(
    session_id: int,
    db: Session = Depends(get_db)
):
    return finish_test_service(
        db=db,
        session_id=session_id
    )