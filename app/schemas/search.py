from pydantic import BaseModel


class SearchResponse(
    BaseModel
):
    id: int

    question_text: str

    topic: str