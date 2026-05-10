from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.schemas.auth import RegisterRequest
from app.schemas.auth import TelegramAuthRequest
from app.schemas.auth import TokenResponse

from app.services.auth_service import create_guest_user
from app.services.auth_service import create_user
from app.services.auth_service import generate_login_response
from app.services.auth_service import get_user_by_telegram_id

from app.utils.validators import validate_full_name

router = APIRouter()


@router.post(
    "/telegram",
    response_model=TokenResponse
)
async def telegram_login(
    payload: TelegramAuthRequest,
    db: Session = Depends(get_db)
):
    user = create_guest_user(
        db=db,
        telegram_id=payload.telegram_id,
        username=payload.username,
    )

    return generate_login_response(user)


@router.post(
    "/register",
    response_model=TokenResponse
)
async def register(
    payload: RegisterRequest,
    db: Session = Depends(get_db)
):
    existing_user = get_user_by_telegram_id(
        db,
        payload.telegram_id
    )

    if existing_user:
        if existing_user.full_name != "NEW_USER":
            raise HTTPException(
                status_code=400,
                detail="User already registered"
            )

        existing_user.full_name = payload.full_name
        existing_user.subject = payload.subject
        existing_user.region = payload.region
        existing_user.school = payload.school

        db.commit()

        db.refresh(existing_user)

        return generate_login_response(
            existing_user
        )

    if not validate_full_name(
        payload.full_name
    ):
        raise HTTPException(
            status_code=400,
            detail="Invalid full name"
        )

    user = create_user(
        db=db,
        telegram_id=payload.telegram_id,
        username=payload.username,
        full_name=payload.full_name,
        subject=payload.subject,
        region=payload.region,
        school=payload.school,
    )

    return generate_login_response(user)