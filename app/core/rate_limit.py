from fastapi import Request
from fastapi import HTTPException

from collections import defaultdict

import time

requests_map = defaultdict(list)

RATE_LIMIT = 100

WINDOW_SECONDS = 60


async def rate_limit_middleware(
    request: Request,
    call_next
):
    ip = request.client.host

    now = time.time()

    requests_map[ip] = [
        req
        for req in requests_map[ip]
        if now - req < WINDOW_SECONDS
    ]

    if (
        len(requests_map[ip])
        >= RATE_LIMIT
    ):
        raise HTTPException(
            status_code=429,
            detail="Too many requests"
        )

    requests_map[ip].append(now)

    response = await call_next(
        request
    )

    return response