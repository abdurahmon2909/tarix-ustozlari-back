from datetime import datetime

from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.core.database import Base


class MilliyCertificateSession(Base):
    __tablename__ = "milliy_certificate_sessions"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    title: Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    subject: Mapped[str] = mapped_column(
        String,
        default="Tarix"
    )

    duration_minutes: Mapped[int] = mapped_column(
        Integer,
        default=120
    )

    total_questions: Mapped[int] = mapped_column(
        Integer,
        default=60
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    starts_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False
    )

    ends_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )