from pydantic import BaseModel
from pydantic import Field


class TelegramAuthRequest(BaseModel):
    init_data: str


class OnboardingRequest(BaseModel):
    full_name: str = Field(
        min_length=5,
        max_length=255
    )

    subject: str

    region: str

    school: str | None = None


class UserResponse(BaseModel):
    id: int

    telegram_id: int

    username: str | None = None

    full_name: str | None = None

    subject: str | None = None

    region: str | None = None

    school: str | None = None

    xp: int

    sharaf: int

    level: int

    streak: int

    onboarding_completed: bool

    role: str

    class Config:
        from_attributes = True


class TokenResponse(BaseModel):
    access_token: str

    refresh_token: str

    token_type: str = "bearer"

    user: UserResponse