import logging
from typing import Optional

from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware

from rest.settings import settings

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

__DISPATCHER__: Optional[Dispatcher] = None


def get_dispatcher() -> Dispatcher:
    global __DISPATCHER__

    if not __DISPATCHER__:
        dispatcher = Dispatcher(
            bot=Bot(settings.TELEGRAM_TOKEN),
            storage=MemoryStorage()
        )
        __DISPATCHER__ = dispatcher

        __setup_dispatcher__(dispatcher=dispatcher)

    return __DISPATCHER__


async def shutdown(dispatcher: Dispatcher):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()


def __setup_dispatcher__(dispatcher: Dispatcher):
    __register_middlewares(dispatcher)
    __register_routes__()
    dispatcher.loop.set_debug(True)


def __register_middlewares(dispatcher: Dispatcher):
    dispatcher.middleware.setup(LoggingMiddleware(logger=logger))


def __register_routes__():
    from .endpoints import commands  # NOQA
    from .endpoints import callbacks  # NOQA
    from .endpoints import states  # NOQA
