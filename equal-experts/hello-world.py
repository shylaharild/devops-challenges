from aiohttp import web
import socket


async def main(request):
    ipadd = socket.gethostbyname(socket.gethostname())
    hw = "Hello, World! " + "IP is : " + ipadd
    print(f'request received: {request} - {ipadd}. response: "{hw}"')
    return web.Response(text=hw)


app = web.Application()
app.router.add_get('/', main)

web.run_app(app, port=3000)
