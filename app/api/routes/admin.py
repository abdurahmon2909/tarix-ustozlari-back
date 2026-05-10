from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.core.dependencies import (
    get_current_admin
)

from app.models.user import User
from app.models.question import Question
from app.models.announcement import Announcement

router = APIRouter()


@router.get("/dashboard")
async def admin_dashboard(
    db: Session = Depends(get_db),
    admin: User = Depends(get_current_admin)
):
    users_count = db.query(
        User
    ).count()

    questions_count = db.query(
        Question
    ).count()

    announcements_count = db.query(
        Announcement
    ).count()

    return {
        "users": users_count,
        "questions": questions_count,
        "announcements": announcements_count,
    }


@router.get("/analytics")
async def analytics(
    admin: User = Depends(get_current_admin)
):
    return {
        "message": "Analytics"
    }