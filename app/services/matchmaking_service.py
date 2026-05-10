from app.core.redis import (
    redis_client
)


MATCHMAKING_QUEUE = "battle_queue"


def join_matchmaking(
    user_id: int
):
    redis_client.rpush(
        MATCHMAKING_QUEUE,
        user_id
    )

    queue_size = redis_client.llen(
        MATCHMAKING_QUEUE
    )

    if queue_size >= 2:
        player1 = redis_client.lpop(
            MATCHMAKING_QUEUE
        )

        player2 = redis_client.lpop(
            MATCHMAKING_QUEUE
        )

        room_id = (
            f"room:{player1}:{player2}"
        )

        return {
            "matched": True,

            "room_id": room_id,

            "players": [
                player1,
                player2
            ]
        }

    return {
        "matched": False
    }