from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.core.database import Base


class Certificate(Base):
    __tablename__ = "certificates"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )

    session_name: Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    grade: Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    percentile: Mapped[float] = mapped_column(
        Float,
        default=0
    )

    score: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    qr_code_url: Mapped[str | None] = mapped_column(
        String,
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )