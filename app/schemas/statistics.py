from pydantic import BaseModel


class StatisticsResponse(
    BaseModel
):
    xp: int

    tests: int

    accuracy: int