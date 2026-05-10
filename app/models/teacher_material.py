from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.core.database import Base


class TeacherMaterial(Base):
    __tablename__ = "teacher_materials"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    teacher_id: Mapped[int] = mapped_column(
        ForeignKey("teachers.id")
    )

    title: Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    file_url: Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    material_type: Mapped[str] = mapped_column(
        String,
        default="pdf"
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )