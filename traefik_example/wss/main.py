import websockets
import asyncio
CLIENTS = set()
siritori_array = []

async def received(websocket):
    global CLIENTS
    global siritori_array
    CLIENTS.add(websocket)
    if len(siritori_array) != 0:
        for item in siritori_array:
            await websocket.send(item)
    async for msg in websocket:
        if len(siritori_array) == 0:
            websockets.broadcast(CLIENTS, msg)
            siritori_array.append(msg)
        elif msg in siritori_array:
            await websocket.send("It's already")
        elif siritori_array[-1][-1] != msg[0]:
            await websocket.send("not equal")
        else:
            websockets.broadcast(CLIENTS, msg)
            siritori_array.append(msg)

async def main():
    async with websockets.serve(received, "", 8081):
        await asyncio.Future()  # run forever

asyncio.run(main())
