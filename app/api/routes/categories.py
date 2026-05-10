from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.services.category_service import (
    get_categories
)

from app.services.category_service import (
    get_subcategories
)

router = APIRouter()


@router.get("/")
async def categories(
    db: Session = Depends(get_db)
):
    return get_categories(
        db=db
    )


@router.get("/{category_id}/subcategories")
async def subcategories(
    category_id: int,
    db: Session = Depends(get_db)
):
    return get_subcategories(
        db=db,
        category_id=category_id
    )