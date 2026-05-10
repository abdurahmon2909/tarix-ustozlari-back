from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.core.database import Base


class ModerationQueue(Base):
    __tablename__ = "moderation_queue"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    question_id: Mapped[int | None] = mapped_column(
        ForeignKey("questions.id"),
        nullable=True
    )

    content_type: Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    content_text: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    status: Mapped[str] = mapped_column(
        String,
        default="pending"
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )