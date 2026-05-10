from pydantic import BaseModel


class DailyChallengeResponse(
    BaseModel
):
    title: str

    xp: int