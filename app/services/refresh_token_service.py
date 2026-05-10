from datetime import datetime
from datetime import timedelta
from uuid import uuid4

from sqlalchemy.orm import Session

from app.models.refresh_token import (
    RefreshToken
)


def create_refresh_token(
    db: Session,
    user_id: int,
    days: int = 30,
):
    token = str(uuid4())

    refresh_token = RefreshToken(
        user_id=user_id,
        token=token,
        expires_at=(
            datetime.utcnow()
            + timedelta(days=days)
        ),
    )

    db.add(refresh_token)

    db.commit()

    db.refresh(refresh_token)

    return refresh_token


def verify_refresh_token(
    db: Session,
    token: str,
):
    refresh_token = db.query(
        RefreshToken
    ).filter(
        RefreshToken.token == token,
        RefreshToken.is_revoked == False
    ).first()

    if not refresh_token:
        return None

    if (
        refresh_token.expires_at
        < datetime.utcnow()
    ):
        return None

    return refresh_token


def revoke_refresh_token(
    db: Session,
    token: str,
):
    refresh_token = db.query(
        RefreshToken
    ).filter(
        RefreshToken.token == token
    ).first()

    if not refresh_token:
        return None

    refresh_token.is_revoked = True

    db.commit()

    db.refresh(refresh_token)

    return refresh_token