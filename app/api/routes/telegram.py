from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.models.telegram_channel import (
    TelegramChannel
)

from app.services.telegram_service import (
    check_user_subscription
)

router = APIRouter()


@router.get("/channels")
async def telegram_channels(
    db: Session = Depends(get_db)
):
    channels = db.query(
        TelegramChannel
    ).filter(
        TelegramChannel.is_required == True
    ).all()

    return channels


@router.get("/check-subscription")
async def check_subscription(
    telegram_user_id: int,
    channel_username: str,
):
    subscribed = await check_user_subscription(
        channel_username=channel_username,
        telegram_user_id=telegram_user_id,
    )

    return {
        "subscribed": subscribed
    }