from pydantic import BaseModel
from pydantic import ConfigDict


class BookResponse(
    BaseModel
):
    model_config = ConfigDict(
        from_attributes=True
    )

    id: int

    title: str

    subject: str


class ChapterResponse(
    BaseModel
):
    model_config = ConfigDict(
        from_attributes=True
    )

    id: int

    title: str