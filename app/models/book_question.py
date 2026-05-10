from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.core.database import Base


class BookQuestion(Base):
    __tablename__ = "book_questions"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    book_id: Mapped[int] = mapped_column(
        ForeignKey("books.id")
    )

    chapter_id: Mapped[int | None] = mapped_column(
        ForeignKey("book_chapters.id"),
        nullable=True
    )

    question_id: Mapped[int] = mapped_column(
        ForeignKey("questions.id")
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )