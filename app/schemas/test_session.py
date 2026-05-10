from pydantic import BaseModel


class TestSessionCreate(BaseModel):
    user_id: int
    session_type: str

    subject: str
    class_name: str

    topic: str | None = None

    total_questions: int
    correct_answers: int


class TestSessionResponse(BaseModel):
    id: int

    score: int
    xp_earned: int

    total_questions: int
    correct_answers: int

    class Config:
        from_attributes = True