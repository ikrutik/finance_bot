from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ParseMode

from interfaces.finance_interface import FinanceBotInterface
from libs import keyboard
from libs.keyboard import PurchaseStates
from rest.applications.aiogram.bootstrap import get_dispatcher
import aiogram.utils.markdown as md
import emoji

dispatcher = get_dispatcher()


@dispatcher.message_handler(commands=['add'])
async def add_command(message: types.Message):
    await PurchaseStates.category.set()
    await message.reply("Выберите категорию", reply_markup=keyboard.keyboard_categories)


@dispatcher.message_handler(commands=['help'])
async def get_help(msg: types.Message):

    message = md.text(
        md.text('C помощью бота вы сможете:',),
        md.text('{} Добавить покупку'.format(emoji.emojize(':zipper-mouth_face:'))),
        md.text('Основные команды:'),
        md.text('Основные команды:'),
        md.text(''),
        md.text('Основные команды:'),
        md.text('/add \- Добавление покупки'),
        md.text('/today \- Остаток на сегодня'),
        md.text('/month \- Остаток на месяц'),
        md.text('/purchase \- Показать покупки'),
        md.text('/help \- Помощь'),
        sep='\n',
    )
    await dispatcher.bot.send_message(
        chat_id=msg.from_user.id,
        text=message,
        parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=keyboard.keyboard_menu

    )


# @dispatcher.message_handler(commands=['add'])
# async def add_command(message: types.Message):
#     await FinanceBotInterface().add_purchase(message)


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
