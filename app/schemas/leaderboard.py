from pydantic import BaseModel


class LeaderboardUserResponse(
    BaseModel
):
    id: int

    full_name: str

    xp: int