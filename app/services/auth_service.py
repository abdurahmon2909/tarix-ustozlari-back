from urllib.parse import parse_qs

from sqlalchemy.orm import Session

from app.models.user import User

from app.core.security import (
    create_access_token,
    create_refresh_token
)


def telegram_auth_service(
    db: Session,
    init_data: str
):
    parsed = parse_qs(init_data)

    user_data = {}

    for key, value in parsed.items():
        user_data[key] = value[0]

    telegram_id = int(
        user_data.get("id", 0)
    )

    username = user_data.get(
        "username"
    )

    first_name = user_data.get(
        "first_name",
        ""
    )

    if not telegram_id:
        raise Exception(
            "Invalid telegram data"
        )

    user = (
        db.query(User)
        .filter(
            User.telegram_id == telegram_id
        )
        .first()
    )

    if not user:
        user = User(
            telegram_id=telegram_id,
            username=username,
            full_name=None,
            onboarding_completed=False
        )

        db.add(user)

        db.commit()

        db.refresh(user)

    access_token = create_access_token(
        {
            "telegram_id": user.telegram_id
        }
    )

    refresh_token = create_refresh_token(
        {
            "telegram_id": user.telegram_id
        }
    )

    return {
        "access_token": access_token,

        "refresh_token": refresh_token,

        "user": {
            "id": user.id,
            "telegram_id": user.telegram_id,
            "username": user.username,
            "full_name": user.full_name,
            "subject": user.subject,
            "region": user.region,
            "school": user.school,
            "xp": user.xp,
            "sharaf": user.sharaf,
            "level": user.level,
            "streak": user.streak,
            "onboarding_completed": user.onboarding_completed,
            "role": user.role
        }
    }