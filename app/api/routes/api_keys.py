from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.services.api_key_service import (
    generate_api_key
)

router = APIRouter()


@router.post("/")
async def api_key_create(
    name: str,
    db: Session = Depends(get_db)
):
    return generate_api_key(
        db=db,
        name=name
    )