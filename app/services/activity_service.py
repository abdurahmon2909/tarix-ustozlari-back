from sqlalchemy.orm import Session

from app.models.activity_log import (
    ActivityLog
)


def log_activity(
    db: Session,
    action: str,
    user_id: int | None = None,
    details: str | None = None,
    ip_address: str | None = None,
):
    log = ActivityLog(
        user_id=user_id,
        action=action,
        details=details,
        ip_address=ip_address,
    )

    db.add(log)

    db.commit()

    db.refresh(log)

    return log