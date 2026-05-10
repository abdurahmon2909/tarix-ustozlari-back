from sqlalchemy.orm import Session

from app.models.user_statistics import (
    UserStatistics
)


def get_leaderboard_service(
    db: Session
):
    leaderboard = db.query(
        UserStatistics
    ).order_by(
        UserStatistics.xp.desc()
    ).limit(50).all()

    return [
        {
            "id": item.user.id,

            "full_name":
                item.user.full_name,

            "xp": item.xp
        }
        for item in leaderboard
    ]