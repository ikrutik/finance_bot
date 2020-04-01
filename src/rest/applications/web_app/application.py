import asyncio

import uvloop
from aiohttp import web

from src.rest.applications.web_app import bootstrap
from src.rest.settings import settings

application = bootstrap.get_application()

if __name__ == "__main__":
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    web.run_app(
        app=application,
        host=settings.HOST,
        port=settings.PORT,
        ssl_context=settings.SSL_CONTEXT)
