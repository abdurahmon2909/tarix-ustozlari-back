from datetime import datetime

from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.core.database import Base


class Teacher(Base):
    __tablename__ = "teachers"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    full_name: Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    subject: Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    region: Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    school_name: Mapped[str | None] = mapped_column(
        String,
        nullable=True
    )

    experience_years: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    is_verified: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )