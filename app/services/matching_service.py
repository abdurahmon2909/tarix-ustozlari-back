from sqlalchemy.orm import Session

from app.models.matching_question import (
    MatchingQuestion
)


def get_matching_questions(
    db: Session
):
    return db.query(
        MatchingQuestion
    ).all()