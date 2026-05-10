from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.services.news_service import (
    get_news
)

from app.services.news_service import (
    create_news
)

router = APIRouter()


@router.get("/")
async def news(
    db: Session = Depends(get_db)
):
    return get_news(
        db=db
    )


@router.post("/")
async def news_create(
    title: str,
    content: str,
    image_url: str | None = None,
    db: Session = Depends(get_db)
):
    return create_news(
        db=db,
        title=title,
        content=content,
        image_url=image_url,
    )