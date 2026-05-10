from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.schemas.auth import (
    TelegramAuthRequest,
    TokenResponse
)

from app.services.auth_service import (
    telegram_auth_service
)

router = APIRouter()


@router.post(
    "/telegram",
    response_model=TokenResponse
)
async def telegram_login(
    payload: TelegramAuthRequest,
    db: Session = Depends(get_db)
):
    return telegram_auth_service(
        db=db,
        telegram_id=payload.telegram_id,
        username=payload.username
    )