from datetime import datetime

from sqlalchemy.orm import Session

from app.models.subscription import (
    Subscription
)

from app.models.user import User


def check_expired_subscriptions(
    db: Session
):
    subscriptions = db.query(
        Subscription
    ).filter(
        Subscription.is_active == True
    ).all()

    now = datetime.utcnow()

    for subscription in subscriptions:
        if (
            subscription.expires_at
            and subscription.expires_at < now
        ):
            subscription.is_active = False

            user = db.query(User).filter(
                User.id == subscription.user_id
            ).first()

            if user:
                user.is_premium = False

    db.commit()