from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import JSON
from sqlalchemy import String
from sqlalchemy import Text

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.core.database import Base


class TableAnalysisQuestion(Base):
    __tablename__ = "table_analysis_questions"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    question_text: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    table_data: Mapped[dict] = mapped_column(
        JSON,
        nullable=False
    )

    correct_answer: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    topic: Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    difficulty: Mapped[str] = mapped_column(
        String,
        default="medium"
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )