import asyncio
from contextlib import suppress
import websockets


async def client(url: str):
    async with websockets.connect(url) as websocket:
        while True:
            message = input("> ")
            await websocket.send(message)
            response = await websocket.recv()
            print(response)


with suppress(KeyboardInterrupt):
    # See asyncio docs for the Python 3.6 equivalent to .run().
    asyncio.run(client("ws://localhost:8000/ws"))