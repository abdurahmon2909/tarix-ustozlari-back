from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.core.database import Base


class Topic(Base):
    __tablename__ = "topics"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    book_id: Mapped[int] = mapped_column(
        ForeignKey("books.id")
    )

    title: Mapped[str] = mapped_column(
        String,
        nullable=False
    )