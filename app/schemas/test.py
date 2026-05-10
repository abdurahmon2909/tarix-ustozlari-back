from pydantic import BaseModel
from pydantic import ConfigDict


class TestResponse(
    BaseModel
):
    model_config = ConfigDict(
        from_attributes=True
    )

    id: int

    title: str

    topic: str

    difficulty: str = "medium"


class StartTestRequest(
    BaseModel
):
    test_id: int

    user_id: int


class StartTestResponse(
    BaseModel
):
    id: int

    status: str


class SubmitAnswerRequest(
    BaseModel
):
    session_id: int

    question_id: int

    selected_answer: str


class SubmitAnswerResponse(
    BaseModel
):
    correct: bool


class QuestionResponse(
    BaseModel
):
    model_config = ConfigDict(
        from_attributes=True
    )

    id: int

    question_text: str

    options: list[str]


class SessionQuestionsResponse(
    BaseModel
):
    questions: list[
        QuestionResponse
    ]


class TestResultResponse(
    BaseModel
):
    correct: int

    percentage: int