from fastapi import APIRouter
from fastapi import WebSocket
from fastapi import WebSocketDisconnect

from app.websocket.connection_manager import (
    manager
)

router = APIRouter()


@router.websocket("/ws/battle")
async def battle_socket(
    websocket: WebSocket
):
    await manager.connect(
        websocket
    )

    try:
        while True:
            data = await websocket.receive_text()

            await manager.broadcast(
                f"Battle: {data}"
            )

    except WebSocketDisconnect:
        manager.disconnect(
            websocket
        )