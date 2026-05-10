from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.services.settings_service import (
    get_setting
)

from app.services.settings_service import (
    set_setting
)

router = APIRouter()


@router.get("/{key}")
async def setting(
    key: str,
    db: Session = Depends(get_db)
):
    return get_setting(
        db=db,
        key=key
    )


@router.post("/")
async def create_setting(
    key: str,
    value: str,
    description: str | None = None,
    db: Session = Depends(get_db)
):
    return set_setting(
        db=db,
        key=key,
        value=value,
        description=description,
    )