from sqlalchemy import ForeignKey
from sqlalchemy import Integer

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.core.database import Base


class ArenaMatchQuestion(Base):
    __tablename__ = "arena_match_questions"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    match_id: Mapped[int] = mapped_column(
        ForeignKey("arena_matches.id")
    )

    question_id: Mapped[int] = mapped_column(
        ForeignKey("questions.id")
    )