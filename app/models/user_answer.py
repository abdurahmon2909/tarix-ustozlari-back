from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy import ForeignKey

from app.models.base import Base


class UserAnswer(Base):
    __tablename__ = "user_answers"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )

    question_id: Mapped[int] = mapped_column(
        ForeignKey("questions.id")
    )

    selected_answer: Mapped[str] = (
        mapped_column(
            String(255)
        )
    )

    is_correct: Mapped[bool] = (
        mapped_column(
            Boolean,
            default=False
        )
    )