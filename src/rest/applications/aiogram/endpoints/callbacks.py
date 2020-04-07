from aiogram import types

from libs import keyboard
from libs.keyboard import PurchaseStates
from rest.applications.aiogram.bootstrap import get_dispatcher

dispatcher = get_dispatcher()


@dispatcher.callback_query_handler(lambda c: c.data and c.data == 'add')
async def process_callback_add(callback_query: types.CallbackQuery):
    await dispatcher.bot.answer_callback_query(callback_query.id)
    await PurchaseStates.category.set()
    await callback_query.message.reply(
        text="Выберите категорию",
        reply_markup=keyboard.keyboard_categories
    )
