from sqlalchemy.orm import Session

from app.models.user_statistics import (
    UserStatistics
)


def add_xp_service(
    db: Session,
    user_id: int,
    xp: int
):
    statistics = db.query(
        UserStatistics
    ).filter(
        UserStatistics.user_id
        == user_id
    ).first()

    if not statistics:
        return

    statistics.xp += xp

    db.commit()