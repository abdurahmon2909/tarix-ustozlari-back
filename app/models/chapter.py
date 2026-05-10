from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

from app.models.base import Base


class Chapter(Base):
    __tablename__ = "chapters"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    title: Mapped[str] = mapped_column(
        String(255)
    )

    book_id: Mapped[int] = mapped_column(
        ForeignKey("books.id")
    )