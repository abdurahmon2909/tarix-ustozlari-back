from pydantic import BaseModel


class CertificateResponse(BaseModel):
    id: int

    session_name: str
    grade: str

    percentile: float
    score: int

    qr_code_url: str | None = None

    class Config:
        from_attributes = True