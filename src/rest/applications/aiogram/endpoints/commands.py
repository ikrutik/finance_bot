from aiogram import types
from aiogram.types import ParseMode

from domains.types import HELP_DESCRIPTION
from interfaces.finance_interface import FinanceBotInterface
from libs import keyboard
from libs.keyboard import PurchaseStates
from rest.applications.aiogram.bootstrap import get_dispatcher

dispatcher = get_dispatcher()


@dispatcher.message_handler(commands=['add'])
async def add_command(message: types.Message):
    await PurchaseStates.category.set()
    await message.reply(
        text="🚥🎲Выберите категорию",
        reply_markup=keyboard.keyboard_categories
    )


@dispatcher.message_handler(commands=['balance'])
async def get_balance_today(message: types.Message):
    await FinanceBotInterface().get_today_balance(
        message=message
    )


@dispatcher.message_handler(commands=['purchases'])
async def get_purchases_today(message: types.Message):
    await FinanceBotInterface().get_today_purchases(
        message=message
    )


@dispatcher.message_handler(commands=['menu'])
async def get_menu(message: types.Message):
    await dispatcher.bot.send_message(
        chat_id=message.from_user.id,
        text='🚪Добро пожаловать',
        reply_markup=keyboard.keyboard_menu
    )


@dispatcher.message_handler(commands=['reset'])
async def reset_state(message: types.Message):
    current_state = dispatcher.current_state(
        user=message.from_user.id
    )
    if current_state is not None:
        await current_state.reset_data()
        await current_state.finish()

    await dispatcher.bot.send_message(
        chat_id=message.from_user.id,
        text='⚙️Успешный сброс',
        reply_markup=keyboard.keyboard_menu
    )


@dispatcher.message_handler(commands=['help'])
async def get_help(message: types.Message):
    await dispatcher.bot.send_message(
        chat_id=message.from_user.id,
        text=HELP_DESCRIPTION,
        parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=keyboard.keyboard_menu
    )


@dispatcher.message_handler()
async def echo_message(msg: types.Message):
    await dispatcher.bot.send_message(msg.from_user.id, msg.text)
