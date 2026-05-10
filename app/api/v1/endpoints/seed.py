from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import (
    get_db
)

from app.services.seed_service import (
    seed_books_service
)

router = APIRouter()


@router.post("")
async def seed_database(
    db: Session = Depends(get_db)
):
    seed_books_service(db)

    return {
        "success": True
    }