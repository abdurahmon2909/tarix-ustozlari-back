from pydantic import BaseModel


class BattleCreate(BaseModel):
    user_id: int


class BattleResponse(BaseModel):
    id: int

    user_id: int
    opponent_id: int | None

    user_score: int
    opponent_score: int

    winner_id: int | None

    status: str

    class Config:
        from_attributes = True