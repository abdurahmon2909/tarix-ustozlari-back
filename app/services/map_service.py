from sqlalchemy.orm import Session

from app.models.map_question import (
    MapQuestion
)


def get_map_questions(
    db: Session
):
    return db.query(
        MapQuestion
    ).all()