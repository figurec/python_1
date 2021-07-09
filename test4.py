#google - heroku python socket
#https://stackoverflow.com/questions/60583950/python-socket-server-in-heroku
#google - What HTTP Headers is my browser sending
#get headers - http://www.xhaus.com/headers
# websocket client - https://websocket.org/echo.html

import asyncio
import os

import websockets

async def echo(websocket, path):
    async for message in websocket:
        await websocket.send(message)

start_server = websockets.serve(echo, "", int(os.environ["PORT"]))

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
