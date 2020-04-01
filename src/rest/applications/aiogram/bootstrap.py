from typing import Optional

from aiogram import Dispatcher, Bot

from rest.settings import settings

__DISPATCHER__: Optional[Dispatcher] = None


def get_dispatcher() -> Dispatcher:
    global __DISPATCHER__

    bot = Bot(token=settings.TELEGRAM_TOKEN)
    if not __DISPATCHER__:
        __DISPATCHER__ = Dispatcher(bot=bot)
        __register_routes__()

    return __DISPATCHER__


def __register_routes__():
    from .endpoints import echo  # noqa
