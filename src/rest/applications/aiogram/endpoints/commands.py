from aiogram import types

from interfaces.finance_interface import FinanceBotInterface
from rest.applications.aiogram.bootstrap import get_dispatcher

dispatcher = get_dispatcher()


@dispatcher.message_handler(commands=['add'])
async def add_command(message: types.Message):
    return await FinanceBotInterface().add_purchase(message)

    # await message.reply('Success')


@dispatcher.message_handler(commands=['today'])
async def get_balance_today(message: types.Message):
    return await FinanceBotInterface().get_today_balance(message)


@dispatcher.message_handler(commands=['month'])
async def get_balance_month(message: types.Message):
    return await FinanceBotInterface().get_month_balance(message)
