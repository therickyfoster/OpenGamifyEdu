from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.sandbox import execute_code

router = APIRouter()

def register_routes(app):
    app.include_router(router)

@router.post("/run-code")
async def run_code(request: dict):
    language = request.get("language")
    code = request.get("code")
    return await execute_code(language, code)

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Echo: {data}")
    except WebSocketDisconnect:
        pass
