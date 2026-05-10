from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import ForeignKey

from app.models.base import Base


class UserStatistics(Base):
    __tablename__ = "user_statistics"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        unique=True
    )

    xp: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    tests: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    accuracy: Mapped[float] = mapped_column(
        Float,
        default=0
    )

    user = relationship(
        "User",
        back_populates="statistics"
    )