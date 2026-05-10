from sqlalchemy.orm import Session

from app.models.daily_challenge import (
    DailyChallenge
)


def get_today_challenge(
    db: Session
):
    challenge = db.query(
        DailyChallenge
    ).order_by(
        DailyChallenge.created_at.desc()
    ).first()

    return challenge