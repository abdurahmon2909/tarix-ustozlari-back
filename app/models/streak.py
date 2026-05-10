from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.core.database import Base


class Streak(Base):
    __tablename__ = "streaks"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        unique=True
    )

    current_streak: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    longest_streak: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    last_activity_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True
    )