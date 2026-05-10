from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.services.metrics_service import (
    get_metrics
)

router = APIRouter()


@router.get("/")
async def metrics(
    db: Session = Depends(get_db)
):
    return get_metrics(
        db=db
    )