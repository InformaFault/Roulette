import asyncio
import ssl
import websockets

class slide:
    def __init__(self, token: str) -> None:
        self.auth = token

    async def bet(self, color: str, amount: int):
        ssl_context = ssl.create_default_context()
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0",
        }
    
        async with websockets.connect("wss://ws.bloxflip.com/socket.io/?EIO=3&transport=websocket", ssl=ssl_context, extra_headers=headers) as ws:
            await ws.send("40/rouletteV2,")
            await ws.send(f'42/rouletteV2,["auth","{token}"]')
            await ws.send('42/rouletteV2,["join-game",{{"color":"{}","betAmount":{}}}]'.format(color, amount))


            message = await ws.recv()
        print(f"Received: {message}")