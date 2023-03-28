import websockets
import asyncio
CLIENTS = set()

async def received(websocket):
    global CLIENTS
    CLIENTS.add(websocket)
    async for msg in websocket:
        websockets.broadcast(CLIENTS, msg)

async def main():
    async with websockets.serve(received, "", 8082):
        await asyncio.Future()  # run forever

asyncio.run(main())
