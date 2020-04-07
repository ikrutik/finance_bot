from aiogram import types
from aiogram.types import ParseMode

from domains.types import HELP_DESCRIPTION
from interfaces.finance_interface import FinanceBotInterface
from libs import keyboard
from libs.keyboard import PurchaseStates
from rest.applications.aiogram.bootstrap import get_dispatcher

dispatcher = get_dispatcher()


@dispatcher.message_handler(commands=['help'])
async def get_help(msg: types.Message):
    await dispatcher.bot.send_message(
        chat_id=msg.from_user.id,
        text=HELP_DESCRIPTION,
        parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=keyboard.keyboard_menu
    )


@dispatcher.message_handler(commands=['add'])
async def add_command(message: types.Message):
    await PurchaseStates.category.set()
    await message.reply("Выберите категорию", reply_markup=keyboard.keyboard_categories)


@dispatcher.message_handler(commands=['today'])
async def get_balance_today(message: types.Message):
    await FinanceBotInterface().get_today_balance(message)


@dispatcher.message_handler(commands=['month'])
async def get_balance_month(message: types.Message):
    await FinanceBotInterface().get_month_balance(message)


@dispatcher.message_handler(commands=['purchase'])
async def get_purchase(message: types.Message):
    await FinanceBotInterface().get_month_balance(message)


@dispatcher.message_handler()
async def echo_message(msg: types.Message):
    await dispatcher.bot.send_message(msg.from_user.id, msg.text)
