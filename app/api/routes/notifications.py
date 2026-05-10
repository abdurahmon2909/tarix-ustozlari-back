from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.schemas.notification import (
    NotificationResponse
)

from app.services.notification_service import (
    get_user_notifications
)

router = APIRouter()


@router.get(
    "/{user_id}",
    response_model=list[
        NotificationResponse
    ]
)
async def notifications(
    user_id: int,
    db: Session = Depends(get_db)
):
    return get_user_notifications(
        db=db,
        user_id=user_id
    )