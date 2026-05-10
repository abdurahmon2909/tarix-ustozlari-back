from pydantic import BaseModel


class TeacherCreateSchema(BaseModel):
    full_name: str

    subject: str

    region: str

    school_name: str | None = None

    experience_years: int = 0