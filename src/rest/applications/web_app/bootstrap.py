import logging.config

from aiohttp import web

from src.rest.applications.web_app.midllewares.factory import middleware_factory
from src.rest.settings import settings

logger = logging.getLogger(__name__)


async def get_application() -> web.Application:
    """ Создание приложения """

    application = web.Application(
        debug=settings.DEBUG,
        middlewares=middleware_factory()
    )

    __register_routes__(application)
    return application


def __register_routes__(application: web.Application):
    """
    Регистрируем HTTP API/роуты
    :return:
    """
    from src.rest.applications.web_app.endpoints.index import routes as index_routes

    application.router.add_routes(index_routes)
