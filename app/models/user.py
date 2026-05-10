from datetime import datetime

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy import DateTime

from app.models.base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    telegram_id: Mapped[int] = mapped_column(
        Integer,
        unique=True,
        index=True
    )

    username: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    full_name: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    subject: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    region: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    school: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    avatar_url: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True
    )

    role: Mapped[str] = mapped_column(
        String(50),
        default="student"
    )

    xp: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    sharaf: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    level: Mapped[int] = mapped_column(
        Integer,
        default=1
    )

    streak: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    onboarding_completed: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    statistics = relationship(
        "UserStatistics",
        back_populates="user",
        uselist=False
    )