from aiogram.utils import executor

from rest.applications.aiogram import bootstrap

if __name__ == '__main__':
    executor.start_polling(
        dispatcher=bootstrap.get_dispatcher(),
        skip_updates=True,
        on_shutdown=bootstrap.shutdown
    )
