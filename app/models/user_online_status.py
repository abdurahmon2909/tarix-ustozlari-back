from datetime import datetime

from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.core.database import Base


class UserOnlineStatus(Base):
    __tablename__ = "user_online_status"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        unique=True
    )

    is_online: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    last_seen_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True
    )