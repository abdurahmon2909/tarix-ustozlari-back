from datetime import datetime
from datetime import timedelta

from sqlalchemy.orm import Session

from app.models.streak import Streak


def update_streak(
    db: Session,
    user_id: int
):
    streak = db.query(
        Streak
    ).filter(
        Streak.user_id == user_id
    ).first()

    now = datetime.utcnow()

    if not streak:
        streak = Streak(
            user_id=user_id,
            current_streak=1,
            longest_streak=1,
            last_activity_at=now,
        )

        db.add(streak)

        db.commit()

        db.refresh(streak)

        return streak

    if streak.last_activity_at:
        difference = (
            now.date()
            - streak.last_activity_at.date()
        ).days

        if difference == 1:
            streak.current_streak += 1

        elif difference > 1:
            streak.current_streak = 1

    if (
        streak.current_streak
        > streak.longest_streak
    ):
        streak.longest_streak = (
            streak.current_streak
        )

    streak.last_activity_at = now

    db.commit()

    db.refresh(streak)

    return streak