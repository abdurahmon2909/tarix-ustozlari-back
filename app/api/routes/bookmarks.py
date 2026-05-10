from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.services.bookmark_service import (
    add_bookmark
)

from app.services.bookmark_service import (
    get_bookmarks
)

router = APIRouter()


@router.post("/")
async def bookmark_add(
    user_id: int,
    question_id: int,
    db: Session = Depends(get_db)
):
    return add_bookmark(
        db=db,
        user_id=user_id,
        question_id=question_id,
    )


@router.get("/{user_id}")
async def bookmarks(
    user_id: int,
    db: Session = Depends(get_db)
):
    return get_bookmarks(
        db=db,
        user_id=user_id
    )