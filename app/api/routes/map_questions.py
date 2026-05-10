from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.services.map_service import (
    get_map_questions
)

router = APIRouter()


@router.get("/")
async def map_questions(
    db: Session = Depends(get_db)
):
    return get_map_questions(
        db=db
    )