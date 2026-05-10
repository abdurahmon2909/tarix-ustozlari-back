from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Text

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.core.database import Base


class QuestionExplanation(Base):
    __tablename__ = "question_explanations"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    question_id: Mapped[int] = mapped_column(
        ForeignKey("questions.id")
    )

    explanation_text: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )