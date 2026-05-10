from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.core.database import Base


class QuestionImport(Base):
    __tablename__ = "question_imports"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    question_text: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    question_type: Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    difficulty: Mapped[str] = mapped_column(
        String,
        default="medium"
    )

    confidence_score: Mapped[float] = mapped_column(
        Float,
        default=0
    )

    processing_status: Mapped[str] = mapped_column(
        String,
        default="pending"
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )