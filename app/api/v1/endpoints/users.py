from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import (
    get_db
)

from app.schemas.auth import (
    UserResponse
)

from app.services.user_service import (
    get_user_profile_service
)

router = APIRouter()


@router.get(
    "/{user_id}",
    response_model=UserResponse
)
async def profile(
    user_id: int,
    db: Session = Depends(get_db)
):
    return get_user_profile_service(
        db=db,
        user_id=user_id
    )