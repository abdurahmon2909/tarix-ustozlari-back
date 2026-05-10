from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

from app.models.base import Base


class Question(Base):
    __tablename__ = "questions"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    question_text: Mapped[str] = (
        mapped_column(
            String(1000)
        )
    )

    option_a: Mapped[str] = (
        mapped_column(
            String(255)
        )
    )

    option_b: Mapped[str] = (
        mapped_column(
            String(255)
        )
    )

    option_c: Mapped[str] = (
        mapped_column(
            String(255)
        )
    )

    option_d: Mapped[str] = (
        mapped_column(
            String(255)
        )
    )

    correct_answer: Mapped[str] = (
        mapped_column(
            String(255)
        )
    )

    correct_count: Mapped[int] = (
        mapped_column(
            Integer,
            default=0
        )
    )

    wrong_count: Mapped[int] = (
        mapped_column(
            Integer,
            default=0
        )
    )

    book_id: Mapped[int] = mapped_column(
        ForeignKey("books.id")
    )

    chapter_id: Mapped[int] = mapped_column(
        ForeignKey("chapters.id")
    )

    @property
    def options(self):
        return [
            self.option_a,
            self.option_b,
            self.option_c,
            self.option_d
        ]