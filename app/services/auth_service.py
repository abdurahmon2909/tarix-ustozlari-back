from sqlalchemy.orm import Session

from app.models.user import User

from app.core.security import (
    create_access_token
)


def telegram_auth_service(
    db: Session,
    telegram_id: int,
    username: str
):
    user = db.query(User).filter(
        User.telegram_id == telegram_id
    ).first()

    if not user:
        user = User(
            telegram_id=telegram_id,
            username=username,
            full_name=username
        )

        db.add(user)

        db.commit()

        db.refresh(user)

    token = create_access_token(
        {
            "sub": str(user.id)
        }
    )

    return {
        "access_token": token,

        "user": {
            "id": user.id,

            "username": user.username,

            "full_name": user.full_name
        }
    }