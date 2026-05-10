from sqlalchemy.orm import Session

from app.models.achievement import (
    Achievement
)

from app.models.user_achievement import (
    UserAchievement
)

from app.models.user_statistics import (
    UserStatistics
)


def check_achievements_service(
    db: Session,
    user_id: int
):
    statistics = db.query(
        UserStatistics
    ).filter(
        UserStatistics.user_id
        == user_id
    ).first()

    if not statistics:
        return

    achievements = db.query(
        Achievement
    ).all()

    for achievement in achievements:
        already_exists = db.query(
            UserAchievement
        ).filter(
            UserAchievement.user_id
            == user_id,

            UserAchievement
            .achievement_id
            == achievement.id
        ).first()

        if already_exists:
            continue

        if (
            statistics.xp
            >= achievement.required_xp
        ):
            unlocked = UserAchievement(
                user_id=user_id,

                achievement_id=
                    achievement.id
            )

            db.add(unlocked)

    db.commit()