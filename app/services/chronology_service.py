from sqlalchemy.orm import Session

from app.models.chronology_question import (
    ChronologyQuestion
)


def get_chronology_questions(
    db: Session
):
    return db.query(
        ChronologyQuestion
    ).all()