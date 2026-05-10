from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from sqlalchemy import Integer
from sqlalchemy import String

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
        unique=True
    )

    username: Mapped[str | None] = (
        mapped_column(
            String(255),
            nullable=True
        )
    )

    full_name: Mapped[str | None] = (
        mapped_column(
            String(255),
            nullable=True
        )
    )

    role: Mapped[str] = mapped_column(
        String(50),
        default="student"
    )

    statistics = relationship(
        "UserStatistics",
        back_populates="user",
        uselist=False
    )