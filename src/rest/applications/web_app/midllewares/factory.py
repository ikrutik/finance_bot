import logging.config
from time import time

from aiohttp.web import Request, Response
from aiohttp.web import middleware

logger = logging.getLogger(__name__)


def middleware_factory():
    """
    Фабрика генерации среднего слоя обработки запросов
    """

    @middleware
    async def audit_middleware(request: Request, handler) -> Response:
        """
        Логирование вызовов API
        :param request: Запрос
        :param handler: Обработчик
        :return: Ответ
        """
        start = time()
        response = await handler(request)
        duration = time() - start
        return response

    return [audit_middleware]
