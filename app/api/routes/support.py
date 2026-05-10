from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.services.support_service import (
    create_support_ticket
)

from app.services.support_service import (
    get_support_tickets
)

router = APIRouter()


@router.post("/")
async def support(
    user_id: int,
    subject: str,
    message: str,
    db: Session = Depends(get_db)
):
    return create_support_ticket(
        db=db,
        user_id=user_id,
        subject=subject,
        message=message,
    )


@router.get("/")
async def tickets(
    db: Session = Depends(get_db)
):
    return get_support_tickets(
        db=db
    )