from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.services.table_analysis_service import (
    get_table_analysis_questions
)

router = APIRouter()


@router.get("/")
async def table_analysis_questions(
    db: Session = Depends(get_db)
):
    return get_table_analysis_questions(
        db=db
    )