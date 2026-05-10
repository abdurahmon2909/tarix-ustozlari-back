from pydantic import BaseModel


class NotificationResponse(BaseModel):
    id: int

    content: str

    is_read: bool

    class Config:
        from_attributes = True