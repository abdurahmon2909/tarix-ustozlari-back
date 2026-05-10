from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.services.device_service import (
    register_device
)

router = APIRouter()


@router.post("/register")
async def device_register(
    user_id: int,
    device_type: str,
    browser: str | None = None,
    os: str | None = None,
    ip_address: str | None = None,
    db: Session = Depends(get_db)
):
    return register_device(
        db=db,
        user_id=user_id,
        device_type=device_type,
        browser=browser,
        os=os,
        ip_address=ip_address,
    )