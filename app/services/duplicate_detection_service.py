from sqlalchemy.orm import Session

from app.models.question import Question


def find_duplicate_question(
    db: Session,
    question_text: str
):
    questions = db.query(
        Question
    ).all()

    normalized = (
        question_text
        .lower()
        .strip()
    )

    for question in questions:
        existing = (
            question.question_text
            .lower()
            .strip()
        )

        if existing == normalized:
            return question

    return None