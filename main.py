import asyncio
import websockets

async def websocket_client():
    uri = "wss://echo.websocket.events"
    async with websockets.connect(uri) as websocket:
        message = "Hello from client!"
        print(f"Sending: {message}")
        await websocket.send(message)

        response = await websocket.recv()
        print(f"Received: {response}")

asyncio.run(websocket_client())
