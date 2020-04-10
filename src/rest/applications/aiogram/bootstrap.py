import logging
from typing import Optional

from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware

from rest.settings import settings
from rest.settings.settings import StartupMode

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

        __setup_dispatcher__(_dispatcher=dispatcher)

    return __DISPATCHER__


async def startup(_dispatcher: Dispatcher):
    if is_running_as_webhook(_dispatcher=_dispatcher):
        await _dispatcher.bot.set_webhook(
            url=settings.WEBHOOK_URL
        )


async def shutdown(_dispatcher: Dispatcher):
    await _dispatcher.bot.delete_webhook()
    await _dispatcher.storage.close()
    await _dispatcher.storage.wait_closed()


def __setup_dispatcher__(_dispatcher: Dispatcher):
    __register_middlewares(_dispatcher=_dispatcher)
    __register_routes__(_dispatcher=_dispatcher)
    _dispatcher.loop.set_debug(settings.DEBUG)


def __register_middlewares(_dispatcher: Dispatcher):
    _dispatcher.middleware.setup(LoggingMiddleware(logger=logger))


def __register_routes__(_dispatcher: Dispatcher):
    from .endpoints import commands  # NOQA
    from .endpoints import callbacks  # NOQA
    from .endpoints import states  # NOQA


def is_running_as_webhook(_dispatcher: Dispatcher) -> bool:
    return getattr(_dispatcher, 'run_mode', StartupMode.POOLING.value) == StartupMode.WEBHOOK.value
