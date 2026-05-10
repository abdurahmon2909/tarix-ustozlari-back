from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.services.ai_recommendation_service import (
    generate_ai_recommendations
)

router = APIRouter()


@router.post("/{user_id}")
async def ai_recommendations(
    user_id: int,
    db: Session = Depends(get_db)
):
    return generate_ai_recommendations(
        db=db,
        user_id=user_id
    )