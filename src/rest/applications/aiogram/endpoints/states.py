from aiogram import types
from aiogram.dispatcher import FSMContext

from libs import keyboard
from libs.keyboard import PurchaseStates
from rest.applications.aiogram.bootstrap import get_dispatcher

dispatcher = get_dispatcher()


@dispatcher.message_handler(state=PurchaseStates.category)
async def process_category(message: types.Message, state: FSMContext):
    category = message.text
    async with state.proxy() as data:
        data['category'] = category
    await PurchaseStates.next()
    await message.reply(
        text=f'Теперь запишите сумму покупки для категории {category}:',
        reply_markup=keyboard.keyboard_amount
    )


@dispatcher.message_handler(state=PurchaseStates.amount)
async def process_amount(message: types.Message, state: FSMContext):
    amount = message.text

    await PurchaseStates.next()
    await state.update_data(amount=int(amount))

    await message.reply(
        text=f'Описание, если хотите:',
        reply_markup=keyboard.keyboard_description
    )


@dispatcher.message_handler(state=PurchaseStates.description)
async def process_description(message: types.Message, state: FSMContext):
    description = message.text
    await state.update_data(description=description)
    await state.finish()
    await message.reply(text=f'Запись успешно добавлена', reply_markup=keyboard.keyboard_menu)
