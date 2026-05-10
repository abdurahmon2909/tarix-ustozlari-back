from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from sqlalchemy import Integer
from sqlalchemy import Boolean
from sqlalchemy import ForeignKey

from app.models.base import Base


class TestSession(Base):
    __tablename__ = "test_sessions"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )

    test_id: Mapped[int] = mapped_column(
        Integer
    )

    finished: Mapped[bool] = (
        mapped_column(
            Boolean,
            default=False
        )
    )

    correct_answers: Mapped[int] = (
        mapped_column(
            Integer,
            default=0
        )
    )

    wrong_answers: Mapped[int] = (
        mapped_column(
            Integer,
            default=0
        )
    )