from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.core.database import Base


class ArenaMatch(Base):
    __tablename__ = "arena_matches"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    player_one_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )

    player_two_id: Mapped[int | None] = mapped_column(
        ForeignKey("users.id"),
        nullable=True
    )

    winner_id: Mapped[int | None] = mapped_column(
        ForeignKey("users.id"),
        nullable=True
    )

    status: Mapped[str] = mapped_column(
        String,
        default="waiting"
    )

    sharaf_reward: Mapped[int] = mapped_column(
        Integer,
        default=25
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )