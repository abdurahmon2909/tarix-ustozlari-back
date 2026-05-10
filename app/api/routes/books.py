from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.services.book_service import (
    get_books
)

from app.services.book_service import (
    get_book_chapters
)

from app.services.book_service import (
    get_book_questions
)

router = APIRouter()


@router.get("/")
async def books(
    db: Session = Depends(get_db)
):
    return get_books(
        db=db
    )


@router.get("/{book_id}/chapters")
async def chapters(
    book_id: int,
    db: Session = Depends(get_db)
):
    return get_book_chapters(
        db=db,
        book_id=book_id
    )


@router.get("/{book_id}/questions")
async def questions(
    book_id: int,
    chapter_id: int | None = None,
    db: Session = Depends(get_db)
):
    return get_book_questions(
        db=db,
        book_id=book_id,
        chapter_id=chapter_id,
    )