from fastapi import APIRouter
from fastapi import WebSocket
from fastapi import (
    WebSocketDisconnect
)

from app.websockets.connection_manager import (
    manager
)

router = APIRouter()


@router.websocket(
    "/ws/battle/{room_id}"
)
async def battle_socket(
    websocket: WebSocket,
    room_id: str
):
    await manager.connect(
        room_id,
        websocket
    )

    try:
        while True:
            data = await websocket.receive_text()

            await manager.broadcast(
                room_id,
                data
            )

    except WebSocketDisconnect:
        manager.disconnect(
            room_id,
            websocket
        )