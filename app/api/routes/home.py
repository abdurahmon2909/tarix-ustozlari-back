from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.services.home_service import (
    get_home_data
)

router = APIRouter()


@router.get("/{user_id}")
async def home(
    user_id: int,
    db: Session = Depends(get_db)
):
    return get_home_data(
        db=db,
        user_id=user_id
    )