from sqlalchemy.orm import Session

from app.models.user import User

from app.core.exceptions import (
    NotFoundException
)


def get_user_profile_service(
    db: Session,
    user_id: int
):
    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if not user:
        raise NotFoundException(
            "Foydalanuvchi topilmadi"
        )

    return user