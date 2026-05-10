from pydantic import BaseModel


class QuestionBase(BaseModel):
    question_type: str
    subject: str
    class_name: str
    book_name: str
    chapter: str
    topic: str

    question_text: str
    correct_answer: str

    difficulty: str = "medium"

    explanation: str | None = None
    image_url: str | None = None


class QuestionResponse(QuestionBase):
    id: int

    class Config:
        from_attributes = True