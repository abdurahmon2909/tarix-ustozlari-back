from pydantic import BaseModel


class TelegramAuthRequest(
    BaseModel
):
    telegram_id: int

    username: str | None = None


class RegisterRequest(
    BaseModel
):
    telegram_id: int

    username: str | None = None

    full_name: str

    subject: str

    region: str

    school: str | None = None


class UserResponse(
    BaseModel
):
    id: int

    username: str | None = None

    full_name: str | None = None

    role: str = "student"


class TokenResponse(
    BaseModel
):
    access_token: str

    token_type: str = "bearer"

    user: UserResponse