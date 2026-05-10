from datetime import datetime

from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.core.database import Base


class DailyChallengeResult(Base):
    __tablename__ = "daily_challenge_results"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    challenge_id: Mapped[int] = mapped_column(
        ForeignKey("daily_challenges.id")
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )

    completed: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    completed_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True
    )