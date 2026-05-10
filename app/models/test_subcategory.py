from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.core.database import Base


class TestSubcategory(Base):
    __tablename__ = "test_subcategories"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    category_id: Mapped[int] = mapped_column(
        ForeignKey("test_categories.id")
    )

    title: Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    slug: Mapped[str] = mapped_column(
        String,
        unique=True,
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )