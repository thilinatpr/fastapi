import asyncio
import websockets

async def websocket_client():
    uri = "wss://echo.websocket.events"

    while True:  # Retry loop to handle disconnections
        try:
            # Connect to the WebSocket server
            async with websockets.connect(uri) as websocket:
                message = "Hello from client!"
                print(f"Sending: {message}")
                await websocket.send(message)

                while True:
                    response = await websocket.recv()
                    print(f"Received: {response}")

        except websockets.ConnectionClosed:
            print("Connection closed. Retrying...")
            await asyncio.sleep(5)  # Wait for 5 seconds before retrying

if __name__ == "__main__":
    asyncio.run(websocket_client())
