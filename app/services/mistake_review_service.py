from sqlalchemy.orm import Session

from app.models.mistake_review import (
    MistakeReview
)


def save_mistake(
    db: Session,
    user_id: int,
    question_id: int,
    topic: str,
    user_answer: str,
    correct_answer: str,
):
    review = MistakeReview(
        user_id=user_id,
        question_id=question_id,
        topic=topic,
        user_answer=user_answer,
        correct_answer=correct_answer,
    )

    db.add(review)

    db.commit()

    db.refresh(review)

    return review


def get_user_mistakes(
    db: Session,
    user_id: int
):
    return db.query(
        MistakeReview
    ).filter(
        MistakeReview.user_id == user_id
    ).all()