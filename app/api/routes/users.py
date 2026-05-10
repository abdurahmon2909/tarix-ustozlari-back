from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.models.user import User

from app.schemas.user import UserCreate
from app.schemas.user import UserResponse

from app.utils.validators import validate_full_name

router = APIRouter()


@router.post(
    "/register",
    response_model=UserResponse
)
async def register_user(
    payload: UserCreate,
    db: Session = Depends(get_db)
):
    existing_user = db.query(User).filter(
        User.telegram_id == payload.telegram_id
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="User already exists"
        )

    if not validate_full_name(
        payload.full_name
    ):
        raise HTTPException(
            status_code=400,
            detail="Invalid full name"
        )

    user = User(
        telegram_id=payload.telegram_id,
        username=payload.username,
        full_name=payload.full_name,
        subject=payload.subject,
        region=payload.region,
        school=payload.school,
    )

    db.add(user)

    db.commit()

    db.refresh(user)

    return user


@router.get(
    "/{user_id}",
    response_model=UserResponse
)
async def get_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user