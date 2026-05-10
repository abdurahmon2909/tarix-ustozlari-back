from sqlalchemy.orm import Session

from app.models.question import (
    Question
)


def search_questions_service(
    db: Session,
    query: str
):
    return db.query(Question).filter(
        Question.question_text.ilike(
            f"%{query}%"
        )
    ).limit(20).all()