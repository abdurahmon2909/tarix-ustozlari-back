from random import choice

from sqlalchemy.orm import Session

from app.models.quote import Quote
from app.models.ticker_announcement import (
    TickerAnnouncement
)

from app.models.user import User

from app.services.daily_challenge_service import (
    get_today_challenge
)

from app.services.recommendation_service import (
    generate_recommendations
)


def get_home_data(
    db: Session,
    user_id: int
):
    user = db.query(User).filter(
        User.id == user_id
    ).first()

    quotes = db.query(
        Quote
    ).filter(
        Quote.is_active == True
    ).all()

    ticker_items = db.query(
        TickerAnnouncement
    ).filter(
        TickerAnnouncement.is_active == True
    ).order_by(
        TickerAnnouncement.priority.desc()
    ).all()

    daily_challenge = get_today_challenge(
        db
    )

    recommendations = generate_recommendations(
        db=db,
        user_id=user_id
    )

    random_quote = (
        choice(quotes)
        if quotes else None
    )

    return {
        "user": user,
        "quote": random_quote,
        "ticker": ticker_items,
        "daily_challenge": daily_challenge,
        "recommendations": recommendations,
    }