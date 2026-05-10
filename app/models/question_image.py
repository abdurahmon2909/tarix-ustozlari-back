from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.core.database import Base


class QuestionImage(Base):
    __tablename__ = "question_images"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    question_id: Mapped[int] = mapped_column(
        ForeignKey("questions.id")
    )

    image_url: Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    image_type: Mapped[str] = mapped_column(
        String,
        default="general"
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )