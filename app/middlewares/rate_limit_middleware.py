from starlette.middleware.base import (
    BaseHTTPMiddleware
)

from fastapi.responses import JSONResponse

from app.core.rate_limit import (
    check_rate_limit
)


class RateLimitMiddleware(
    BaseHTTPMiddleware
):
    async def dispatch(
        self,
        request,
        call_next
    ):
        client_ip = request.client.host

        try:
            check_rate_limit(
                key=f"rate_limit:{client_ip}"
            )

        except Exception:
            return JSONResponse(
                status_code=429,
                content={
                    "success": False,
                    "message": (
                        "Too many requests"
                    )
                }
            )

        response = await call_next(
            request
        )

        return response