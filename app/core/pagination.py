def paginate(
    query,
    page: int = 1,
    limit: int = 20
):
    offset = (
        page - 1
    ) * limit

    return query.offset(
        offset
    ).limit(
        limit
    ).all()