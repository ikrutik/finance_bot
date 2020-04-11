"""
Callback handlers
"""
from aiogram import types

from domains.types import PurchaseStates
from interfaces.finance_interface import FinanceBotInterface
from libs import keyboard
from rest.applications.aiogram.bootstrap import get_dispatcher

dispatcher = get_dispatcher()


@dispatcher.callback_query_handler(lambda c: c.data and c.data == 'add')
async def process_callback_add(callback_query: types.CallbackQuery):
    await dispatcher.bot.answer_callback_query(
        callback_query_id=callback_query.id
    )
    await PurchaseStates.category.set()

    await dispatcher.bot.send_message(
        chat_id=callback_query.message.chat.id,
        text="🎲Выберите категорию",
        reply_markup=keyboard.keyboard_categories
    )


@dispatcher.callback_query_handler(lambda c: c.data and c.data == 'balance')
async def process_callback_today_balance(callback_query: types.CallbackQuery):
    await dispatcher.bot.answer_callback_query(
        callback_query_id=callback_query.id
    )
    await FinanceBotInterface().get_today_balance(
        message=callback_query.message
    )


@dispatcher.callback_query_handler(lambda c: c.data and c.data == 'purchases')
async def process_callback_today_purchases(callback_query: types.CallbackQuery):
    await dispatcher.bot.answer_callback_query(
        callback_query_id=callback_query.id
    )

    await FinanceBotInterface().get_today_purchases(
        message=callback_query.message
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
