from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.services.portfolio_service import (
    get_user_portfolio
)

router = APIRouter()


@router.get("/{user_id}")
async def portfolio(
    user_id: int,
    db: Session = Depends(get_db)
):
    return get_user_portfolio(
        db=db,
        user_id=user_id
    )