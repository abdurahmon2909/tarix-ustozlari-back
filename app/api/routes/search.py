from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.services.search_service import (
    search_questions
)

router = APIRouter()


@router.get("/")
async def search(
    query: str,
    db: Session = Depends(get_db)
):
    return search_questions(
        db=db,
        query=query
    )