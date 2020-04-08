from aiogram import types

from libs import keyboard
from libs.keyboard import PurchaseStates
from rest.applications.aiogram.bootstrap import get_dispatcher

dispatcher = get_dispatcher()


@dispatcher.callback_query_handler(lambda c: c.data and c.data == 'add')
async def process_callback_add(callback_query: types.CallbackQuery):
    await dispatcher.bot.answer_callback_query(
        callback_query_id=callback_query.id
    )
    await PurchaseStates.category.set()

    await callback_query.message.reply(
        text="Выберите категорию",
        reply_markup=keyboard.keyboard_categories
    )


@dispatcher.callback_query_handler(lambda c: c.data and c.data == 'balance')
async def process_callback_today_balance(callback_query: types.CallbackQuery):
    await dispatcher.bot.answer_callback_query(
        callback_query_id=callback_query.id
    )

    await callback_query.message.reply(
        text="Еще не реализовано",
        reply_markup=keyboard.keyboard_menu
    )


@dispatcher.callback_query_handler(lambda c: c.data and c.data == 'purchases')
async def process_callback_today_purchases(callback_query: types.CallbackQuery):
    await dispatcher.bot.answer_callback_query(
        callback_query_id=callback_query.id
    )

    await callback_query.message.reply(
        text="Еще не реализовано",
        reply_markup=keyboard.keyboard_menu
    )


@dispatcher.message_handler(lambda c: c.data and c.data == 'reset')
async def process_callback_reset_state(callback_query: types.CallbackQuery):

    await dispatcher.bot.answer_callback_query(
        callback_query_id=callback_query.id
    )

    current_state = dispatcher.current_state(
        user=callback_query.message.from_user.id
    )

    if current_state is not None:
        await current_state.reset_data()
        await current_state.finish()

    await dispatcher.bot.send_message(
        chat_id=callback_query.message.from_user.id,
        text='Успешный сброс',
        reply_markup=keyboard.keyboard_menu
    )
