from datetime import datetime

from sqlalchemy.orm import Session

from app.models.user_online_status import (
    UserOnlineStatus
)


def set_online(
    db: Session,
    user_id: int
):
    status = db.query(
        UserOnlineStatus
    ).filter(
        UserOnlineStatus.user_id == user_id
    ).first()

    if not status:
        status = UserOnlineStatus(
            user_id=user_id
        )

        db.add(status)

    status.is_online = True

    status.last_seen_at = (
        datetime.utcnow()
    )

    db.commit()

    db.refresh(status)

    return status


def set_offline(
    db: Session,
    user_id: int
):
    status = db.query(
        UserOnlineStatus
    ).filter(
        UserOnlineStatus.user_id == user_id
    ).first()

    if not status:
        return None

    status.is_online = False

    status.last_seen_at = (
        datetime.utcnow()
    )

    db.commit()

    db.refresh(status)

    return status