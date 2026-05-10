from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.schemas.statistics import (
    UserStatisticsResponse
)

from app.services.statistics_service import (
    get_user_statistics
)

router = APIRouter()


@router.get(
    "/{user_id}",
    response_model=UserStatisticsResponse
)
async def statistics(
    user_id: int,
    db: Session = Depends(get_db)
):
    return get_user_statistics(
        db=db,
        user_id=user_id
    )