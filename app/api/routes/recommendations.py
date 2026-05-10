from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.services.recommendation_service import (
    generate_recommendations
)

router = APIRouter()


@router.get("/{user_id}")
async def recommendations(
    user_id: int,
    db: Session = Depends(get_db)
):
    return generate_recommendations(
        db=db,
        user_id=user_id
    )