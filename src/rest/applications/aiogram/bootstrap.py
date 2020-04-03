from typing import Optional

from aiogram import Dispatcher, Bot

from rest.settings import settings

__DISPATCHER__: Optional[Dispatcher] = None


def get_dispatcher() -> Dispatcher:
    global __DISPATCHER__

    if not __DISPATCHER__:
        bot = Bot(token=settings.TELEGRAM_TOKEN)
        dispatcher = Dispatcher(bot=bot)
        __DISPATCHER__ = dispatcher

        __setup_dispatcher__(dispatcher=dispatcher)

    return __DISPATCHER__


def __setup_dispatcher__(dispatcher: Dispatcher):
    __register_routes__()


def __register_routes__():
    from .endpoints import commands  # noqa
