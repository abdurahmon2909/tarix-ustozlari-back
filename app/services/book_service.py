from sqlalchemy.orm import Session

from app.models.book import Book

from app.models.chapter import (
    Chapter
)

from app.models.question import (
    Question
)

from app.core.exceptions import (
    NotFoundException
)


def get_books_service(
    db: Session
):
    return db.query(Book).all()


def get_book_chapters_service(
    db: Session,
    book_id: int
):
    book = db.query(Book).filter(
        Book.id == book_id
    ).first()

    if not book:
        raise NotFoundException(
            "Kitob topilmadi"
        )

    return db.query(Chapter).filter(
        Chapter.book_id == book_id
    ).all()


def get_book_questions_service(
    db: Session,
    book_id: int
):
    return db.query(Question).filter(
        Question.book_id == book_id
    ).limit(20).all()