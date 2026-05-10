from pydantic import BaseModel


class CertificateSessionResponse(BaseModel):
    id: int

    title: str
    subject: str

    duration_minutes: int
    total_questions: int

    is_active: bool

    class Config:
        from_attributes = True


class CertificateResultResponse(BaseModel):
    id: int

    score: int
    percentage: float

    theta: float
    percentile: float

    grade: str
    rank: int

    class Config:
        from_attributes = True