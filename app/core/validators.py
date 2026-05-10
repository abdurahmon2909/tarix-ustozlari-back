from app.core.exceptions import (
    AppException
)


def validate_pagination(
    page: int,
    limit: int
):
    if page < 1:
        raise AppException(
            "Page noto'g'ri"
        )

    if limit < 1:
        raise AppException(
            "Limit noto'g'ri"
        )