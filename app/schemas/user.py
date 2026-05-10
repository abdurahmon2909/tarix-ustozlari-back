from pydantic import BaseModel
from pydantic import Field


class UserBase(BaseModel):
    full_name: str = Field(
        min_length=3,
        max_length=120
    )

    subject: str
    region: str
    school: str | None = None


class UserCreate(UserBase):
    telegram_id: int
    username: str | None = None


class UserResponse(UserBase):
    id: int
    telegram_id: int
    username: str | None = None

    xp: int
    sharaf: int
    level: int
    streak: int
    accuracy: int
    solved_tests: int

    rank_title: str
    certificate_grade: str | None = None

    avatar_url: str | None = None

    class Config:
        from_attributes = True