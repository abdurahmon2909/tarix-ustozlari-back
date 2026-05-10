import json

from app.core.redis import (
    redis_client
)


def set_cache(
    key: str,
    value,
    expire: int = 300
):
    redis_client.set(
        key,
        json.dumps(value),
        ex=expire
    )


def get_cache(
    key: str
):
    data = redis_client.get(key)

    if not data:
        return None

    return json.loads(data)