from datetime import datetime
from datetime import timedelta

from jose import jwt
from jose import JWTError

from passlib.context import (
    CryptContext
)

from app.core.config import (
    settings
)

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

ALGORITHM = "HS256"


def create_access_token(
    data: dict
):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(
        days=7
    )

    to_encode.update(
        {"exp": expire}
    )

    return jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=ALGORITHM
    )


def decode_access_token(
    token: str
):
    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        return payload

    except JWTError:
        return None