import argparse
import asyncio

import uvloop
from aiogram import Dispatcher
from aiogram.utils import executor
from aiogram.utils.executor import start_webhook

from rest.applications.aiogram import bootstrap
from rest.settings import settings
from rest.settings.settings import StartupMode


def run_webhook_mode(_dispatcher: Dispatcher):
    _dispatcher.run_mode = StartupMode.WEBHOOK.value

    start_webhook(
        dispatcher=_dispatcher,
        on_startup=bootstrap.startup,
        on_shutdown=bootstrap.shutdown,
        host=settings.HOST,
        port=settings.PORT,
        webhook_path=settings.WEBHOOK_PATH,
        skip_updates=settings.SKIP_UPDATES,
    )


def run_pooling_mode(_dispatcher: Dispatcher):
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
        default=StartupMode.WEBHOOK.value
    )

    dispatcher = bootstrap.get_dispatcher()
    if parser.parse_args().mode == StartupMode.WEBHOOK.value:
        run_webhook_mode(_dispatcher=dispatcher)
    else:
        run_pooling_mode(_dispatcher=dispatcher)
