from pydantic import BaseModel


class NewsCreateSchema(BaseModel):
    title: str

    content: str

    image_url: str | None = None