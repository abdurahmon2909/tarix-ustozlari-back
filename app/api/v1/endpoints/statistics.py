from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import (
    get_db
)

from app.schemas.statistics import (
    StatisticsResponse
)

from app.services.statistics_service import (
    get_statistics_service
)

router = APIRouter()


@router.get(
    "/{user_id}",
    response_model=
    StatisticsResponse
)
async def statistics(
    user_id: int,
    db: Session = Depends(get_db)
):
    return get_statistics_service(
        db=db,
        user_id=user_id
    )