from sqlalchemy.orm import Session

from app.models.portfolio_item import (
    PortfolioItem
)

from app.models.user_badge import (
    UserBadge
)

from app.models.historical_badge import (
    HistoricalBadge
)


def get_user_portfolio(
    db: Session,
    user_id: int
):
    items = db.query(
        PortfolioItem
    ).filter(
        PortfolioItem.user_id == user_id
    ).all()

    badges = db.query(
        UserBadge
    ).filter(
        UserBadge.user_id == user_id
    ).all()

    badge_ids = [
        badge.badge_id
        for badge in badges
    ]

    historical_badges = db.query(
        HistoricalBadge
    ).filter(
        HistoricalBadge.id.in_(badge_ids)
    ).all()

    return {
        "portfolio_items": items,
        "badges": historical_badges,
    }