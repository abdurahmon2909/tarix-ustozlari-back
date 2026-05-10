from sqlalchemy.orm import Session

from app.models.book import Book

from app.models.chapter import (
    Chapter
)

from app.models.question import (
    Question
)


def seed_books_service(
    db: Session
):
    book = Book(
        title=
            "7-sinf O'zbekiston tarixi",

        subject="Tarix"
    )

    db.add(book)

    db.commit()

    db.refresh(book)

    chapter = Chapter(
        title="Temuriylar",

        book_id=book.id
    )

    db.add(chapter)

    db.commit()

    question = Question(
        question_text=
            "Amir Temur qachon tug'ilgan?",

        correct_answer="1336",

        option_a="1336",

        option_b="1405",

        option_c="1220",

        option_d="1500",

        chapter_id=chapter.id,

        book_id=book.id
    )

    db.add(question)

    db.commit()