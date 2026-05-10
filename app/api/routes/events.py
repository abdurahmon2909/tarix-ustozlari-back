from datetime import datetime

from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.services.event_service import (
    create_event
)

from app.services.event_service import (
    get_events
)

router = APIRouter()


@router.get("/")
async def events(
    db: Session = Depends(get_db)
):
    return get_events(
        db=db
    )


@router.post("/")
async def event_create(
    title: str,
    description: str,
    event_date: datetime,
    image_url: str | None = None,
    db: Session = Depends(get_db)
):
    return create_event(
        db=db,
        title=title,
        description=description,
        event_date=event_date,
        image_url=image_url,
    )