from sqlalchemy.orm import Session

from app.models.test_history import (
    TestHistory
)


def save_test_history(
    db: Session,
    user_id: int,
    test_session_id: int,
    score: float,
):
    history = TestHistory(
        user_id=user_id,
        test_session_id=test_session_id,
        score=score,
    )

    db.add(history)

    db.commit()

    db.refresh(history)

    return history


def get_user_history(
    db: Session,
    user_id: int
):
    return db.query(
        TestHistory
    ).filter(
        TestHistory.user_id == user_id
    ).all()