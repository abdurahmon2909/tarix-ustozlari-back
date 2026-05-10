from pydantic import BaseModel

from typing import Generic
from typing import TypeVar


T = TypeVar("T")


class PaginationMeta(
    BaseModel
):
    page: int

    limit: int

    total: int

    total_pages: int


class PaginatedResponse(
    BaseModel,
    Generic[T]
):
    success: bool = True

    items: list[T]

    meta: PaginationMeta