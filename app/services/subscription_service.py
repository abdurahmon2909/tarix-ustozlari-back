from datetime import datetime
from datetime import timedelta

from sqlalchemy.orm import Session

from app.models.subscription import (
    Subscription
)

from app.models.user import User


def activate_subscription(
    db: Session,
    user_id: int,
    days: int = 30,
):
    subscription = db.query(
        Subscription
    ).filter(
        Subscription.user_id == user_id
    ).first()

    expires_at = (
        datetime.utcnow()
        + timedelta(days=days)
    )

    if subscription:
        subscription.is_active = True

        subscription.expires_at = (
            expires_at
        )

    else:
        subscription = Subscription(
            user_id=user_id,
            is_active=True,
            expires_at=expires_at,
        )

        db.add(subscription)

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if user:
        user.is_premium = True

    db.commit()

    db.refresh(subscription)

    return subscription