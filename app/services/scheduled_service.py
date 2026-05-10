from sqlalchemy.orm import Session

from app.services.subscription_checker_service import (
    check_expired_subscriptions
)


def run_daily_jobs(
    db: Session
):
    check_expired_subscriptions(
        db=db
    )