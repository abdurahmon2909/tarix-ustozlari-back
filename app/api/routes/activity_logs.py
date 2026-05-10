from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.models.activity_log import (
    ActivityLog
)

router = APIRouter()


@router.get("/")
async def activity_logs(
    db: Session = Depends(get_db)
):
    logs = db.query(
        ActivityLog
    ).order_by(
        ActivityLog.created_at.desc()
    ).limit(100).all()

    return logs