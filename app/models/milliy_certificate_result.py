from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.core.database import Base


class MilliyCertificateResult(Base):
    __tablename__ = "milliy_certificate_results"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )

    session_id: Mapped[int] = mapped_column(
        ForeignKey(
            "milliy_certificate_sessions.id"
        )
    )

    score: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    percentage: Mapped[float] = mapped_column(
        Float,
        default=0
    )

    theta: Mapped[float] = mapped_column(
        Float,
        default=0
    )

    percentile: Mapped[float] = mapped_column(
        Float,
        default=0
    )

    grade: Mapped[str] = mapped_column(
        String,
        default="Fail"
    )

    rank: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )