from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import (
    get_db
)

from app.schemas.book import (
    BookResponse,
    ChapterResponse
)

from app.schemas.test import (
    QuestionResponse
)

from app.services.book_service import (
    get_books_service,
    get_book_chapters_service,
    get_book_questions_service
)

router = APIRouter()


@router.get(
    "",
    response_model=list[
        BookResponse
    ]
)
async def get_books(
    db: Session = Depends(get_db)
):
    return get_books_service(
        db=db
    )


@router.get(
    "/{book_id}/chapters",
    response_model=list[
        ChapterResponse
    ]
)
async def chapters(
    book_id: int,
    db: Session = Depends(get_db)
):
    return get_book_chapters_service(
        db=db,
        book_id=book_id
    )


@router.get(
    "/{book_id}/questions",
    response_model=list[
        QuestionResponse
    ]
)
async def questions(
    book_id: int,
    db: Session = Depends(get_db)
):
    return get_book_questions_service(
        db=db,
        book_id=book_id
    )