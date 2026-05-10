from sqlalchemy.orm import Session

from app.models.open_answer_question import (
    OpenAnswerQuestion
)


def get_open_answer_questions(
    db: Session
):
    return db.query(
        OpenAnswerQuestion
    ).all()


def check_open_answer(
    expected_answer: str,
    user_answer: str
):
    expected = expected_answer.lower().strip()

    user = user_answer.lower().strip()

    return expected in user