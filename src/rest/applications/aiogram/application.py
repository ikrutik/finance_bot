import argparse
import asyncio
from os.path import abspath, dirname, join as path_join
from sys import path as sys_path

import uvloop
from aiogram import Dispatcher
from aiogram.utils import executor
from aiogram.utils.executor import start_webhook

sys_path.insert(0, abspath(path_join(dirname(__file__), "..", "..", "..", "..")))

from src.rest.applications.aiogram import bootstrap  # noqa
from src.rest.settings import settings  # noqa
from src.rest.settings.settings import StartupMode  # noqa


def run_webhook_mode(_dispatcher: Dispatcher, host: str, port: int):
    """ Run as webhook"""

    _dispatcher.run_mode = StartupMode.WEBHOOK.value

    start_webhook(
        dispatcher=_dispatcher,
        on_startup=bootstrap.startup,
        on_shutdown=bootstrap.shutdown,
        host=host or settings.HOST,
        port=port or settings.PORT,
        webhook_path=settings.WEBHOOK_PATH,
        skip_updates=settings.SKIP_UPDATES,
    )


def run_pooling_mode(_dispatcher: Dispatcher):
    """ Run as pooling"""
    _dispatcher.run_mode = StartupMode.POOLING.value

    executor.start_polling(
        dispatcher=_dispatcher,
        on_startup=bootstrap.startup,
        on_shutdown=bootstrap.shutdown,
        skip_updates=settings.SKIP_UPDATES,
        relax=settings.RELAX_TIMEOUT
    )


if __name__ == '__main__':
    asyncio.set_event_loop_policy(
        policy=uvloop.EventLoopPolicy()
    )

    parser = argparse.ArgumentParser(
        description='Режим запуска бота'
    )
    parser.add_argument(
        '--mode',
        help='Режимы запуска бота (pooling, webhook)',
        default=StartupMode.POOLING.value
    )
    parser.add_argument(
        '--host',
        help='Хост запуска приложения',
        default=settings.HOST
    )
    parser.add_argument(
        '--port',
        help='Порт запуска приложения',
        default=settings.PORT
    )

    args = parser.parse_args()
    dispatcher = bootstrap.get_dispatcher()

    if args.mode == StartupMode.WEBHOOK.value:
        run_webhook_mode(_dispatcher=dispatcher, host=args.host, port=args.port)
    else:
        run_pooling_mode(_dispatcher=dispatcher)
