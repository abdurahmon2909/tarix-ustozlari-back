from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.services.matching_service import (
    get_matching_questions
)

router = APIRouter()


@router.get("/")
async def matching_questions(
    db: Session = Depends(get_db)
):
    return get_matching_questions(
        db=db
    )