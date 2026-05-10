from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.services.chronology_service import (
    get_chronology_questions
)

router = APIRouter()


@router.get("/")
async def chronology_questions(
    db: Session = Depends(get_db)
):
    return get_chronology_questions(
        db=db
    )