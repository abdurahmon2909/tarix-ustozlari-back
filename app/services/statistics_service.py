from sqlalchemy.orm import Session

from app.models.user_statistics import (
    UserStatistics
)

from app.core.exceptions import (
    NotFoundException
)


def get_statistics_service(
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
        raise NotFoundException(
            "Statistika topilmadi"
        )

    return statistics