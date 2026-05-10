from pydantic import BaseModel


class AchievementResponse(BaseModel):
    id: int

    title: str
    description: str

    icon: str | None = None

    xp_reward: int

    class Config:
        from_attributes = True