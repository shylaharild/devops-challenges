from aiohttp import web
import socket


async def main(request):
    ipadd = socket.gethostbyname(socket.gethostname())
    text = "Hello, World! " + "IP is : " + ipadd
    print(f'request received: {request} - {ipadd}. response: "{text}"')
    return web.Response(text=text)


app = web.Application()
app.router.add_get('/', main)

web.run_app(app, port=3000)
