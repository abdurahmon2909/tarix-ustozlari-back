from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from app.core.database import Base


class UserAchievement(Base):
    __tablename__ = "user_achievements"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )

    achievement_id: Mapped[int] = mapped_column(
        ForeignKey("achievements.id")
    )

    earned_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )
    difficulty: Mapped[str] = mapped_column(
        String,
        default="medium"
    )

    battle_allowed: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )

    view_count: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    correct_count: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    wrong_count: Mapped[int] = mapped_column(
        Integer,
        default=0
    )