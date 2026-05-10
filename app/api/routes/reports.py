from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.services.report_service import (
    create_report
)

from app.services.report_service import (
    get_reports
)

router = APIRouter()


@router.post("/")
async def report(
    reporter_user_id: int,
    reason: str,
    description: str | None = None,
    reported_question_id: int | None = None,
    db: Session = Depends(get_db)
):
    return create_report(
        db=db,
        reporter_user_id=reporter_user_id,
        reason=reason,
        description=description,
        reported_question_id=reported_question_id,
    )


@router.get("/")
async def reports(
    db: Session = Depends(get_db)
):
    return get_reports(
        db=db
    )