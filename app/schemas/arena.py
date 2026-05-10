from pydantic import BaseModel


class ArenaMatchCreate(BaseModel):
    player_one_id: int


class ArenaMatchResponse(BaseModel):
    id: int

    player_one_id: int
    player_two_id: int | None

    winner_id: int | None

    status: str

    sharaf_reward: int

    class Config:
        from_attributes = True