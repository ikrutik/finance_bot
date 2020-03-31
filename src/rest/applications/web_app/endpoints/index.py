from aiohttp import web
from aiohttp.web import RouteTableDef, Request

routes = RouteTableDef()


@routes.get("/")
async def index(request: Request):
    return web.Response(text="Hello, world!")
