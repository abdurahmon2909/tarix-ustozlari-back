from fastapi import APIRouter

from app.websocket.quiz_room_socket import (
    router as quiz_room_socket_router
)

from app.websocket.battle_socket import (
    router as battle_socket_router
)

from app.websocket.notification_socket import (
    router as notification_socket_router
)

websocket_router = APIRouter()

websocket_router.include_router(
    quiz_room_socket_router
)

websocket_router.include_router(
    battle_socket_router
)

websocket_router.include_router(
    notification_socket_router
)