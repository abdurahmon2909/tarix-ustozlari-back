from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import (
    get_db
)

from app.services.notification_service import (
    create_notification_service
)

router = APIRouter()


@router.post("")
async def create_notification(
    user_id: int,
    title: str,
    message: str,
    db: Session = Depends(get_db)
):
    return create_notification_service(
        db=db,

        user_id=user_id,

        title=title,

        message=message
    )