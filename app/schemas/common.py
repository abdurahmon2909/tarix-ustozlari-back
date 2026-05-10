from pydantic import BaseModel

from typing import Generic
from typing import TypeVar


T = TypeVar("T")


class MessageResponse(
    BaseModel
):
    success: bool = True

    message: str


class DataResponse(
    BaseModel,
    Generic[T]
):
    success: bool = True

    data: T