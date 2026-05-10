import math


def build_pagination(
    page: int,
    limit: int,
    total: int
):
    return {
        "page": page,

        "limit": limit,

        "total": total,

        "total_pages": math.ceil(
            total / limit
        )
    }