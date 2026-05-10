from pydantic import BaseModel


class AnnouncementResponse(BaseModel):
    id: int

    title: str
    content: str

    is_active: bool

    class Config:
        from_attributes = True