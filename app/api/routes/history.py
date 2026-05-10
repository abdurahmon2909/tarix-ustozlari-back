from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.services.history_service import (
    get_user_history
)

router = APIRouter()


@router.get("/{user_id}")
async def history(
    user_id: int,
    db: Session = Depends(get_db)
):
    return get_user_history(
        db=db,
        user_id=user_id
    )