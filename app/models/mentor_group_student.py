from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.core.database import Base


class MentorGroupStudent(Base):
    __tablename__ = "mentor_group_students"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    group_id: Mapped[int] = mapped_column(
        ForeignKey("mentor_groups.id")
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )

    joined_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )