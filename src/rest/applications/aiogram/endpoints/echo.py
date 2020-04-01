from aiogram import types

from rest.applications.aiogram.bootstrap import get_dispatcher

dispatcher = get_dispatcher()


@dispatcher.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)
