from fastapi import APIRouter
from fastapi import WebSocket
from fastapi import WebSocketDisconnect

from app.websocket.connection_manager import (
    manager
)

router = APIRouter()


@router.websocket("/ws/notifications")
async def notification_socket(
    websocket: WebSocket
):
    await manager.connect(
        websocket
    )

    try:
        while True:
            data = await websocket.receive_text()

            await manager.send_personal_message(
                f"Notification: {data}",
                websocket
            )

    except WebSocketDisconnect:
        manager.disconnect(
            websocket
        )