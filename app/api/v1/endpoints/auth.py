from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi.security import HTTPBearer
from fastapi.security import HTTPAuthorizationCredentials

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.core.security import (
    decode_token
)

from app.models.user import User

from app.schemas.auth import (
    TelegramAuthRequest,
    TokenResponse,
    UserResponse,
    OnboardingRequest
)

from app.services.auth_service import (
    telegram_auth_service
)

router = APIRouter()

security = HTTPBearer()


@router.post(
    "/telegram",
    response_model=TokenResponse
)
async def telegram_login(
    payload: TelegramAuthRequest,
    db: Session = Depends(get_db)
):
    return telegram_auth_service(
        db=db,
        init_data=payload.init_data
    )


@router.get(
    "/me",
    response_model=UserResponse
)
async def get_me(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    token = credentials.credentials

    payload = decode_token(token)

    if not payload:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    telegram_id = payload.get(
        "telegram_id"
    )

    user = (
        db.query(User)
        .filter(
            User.telegram_id == telegram_id
        )
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user


@router.post(
    "/onboarding",
    response_model=UserResponse
)
async def onboarding(
    payload: OnboardingRequest,
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    token = credentials.credentials

    decoded = decode_token(token)

    if not decoded:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    telegram_id = decoded.get(
        "telegram_id"
    )

    user = (
        db.query(User)
        .filter(
            User.telegram_id == telegram_id
        )
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    user.full_name = payload.full_name
    user.subject = payload.subject
    user.region = payload.region
    user.school = payload.school
    user.onboarding_completed = True

    db.commit()

    db.refresh(user)

    return user