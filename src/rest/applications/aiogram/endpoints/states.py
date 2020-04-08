from aiogram import types
from aiogram.dispatcher import FSMContext

from interfaces.finance_interface import FinanceBotInterface
from libs import keyboard
from libs.keyboard import PurchaseStates
from rest.applications.aiogram.bootstrap import get_dispatcher

dispatcher = get_dispatcher()


def reset_text_handler(func):
    async def decorator(message: types.Message, state: FSMContext):
        reset_text = keyboard.button_reset.text.lower()
        if message.text.lower() == reset_text:

            if state is not None:
                await state.finish()

            await message.reply(
                text='Успешный сброс',
                reply_markup=keyboard.keyboard_menu
            )
            return

        return await func(message, state)

    return decorator


@dispatcher.message_handler(state=PurchaseStates.category)
@reset_text_handler
async def process_category(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['category'] = message.text

    await PurchaseStates.next()

    await message.reply(
        text='Теперь запишите сумму покупки для категории',
        reply_markup=keyboard.keyboard_amount
    )


@dispatcher.message_handler(lambda message: message.text.isdigit(), state=PurchaseStates.amount)
@reset_text_handler
async def process_amount(message: types.Message, state: FSMContext):
    await PurchaseStates.next()
    await state.update_data(
        amount=int(message.text)
    )
    await message.reply(
        text=f'Напиши описание, если есть желание:',
        reply_markup=keyboard.keyboard_description
    )


@dispatcher.message_handler(state=PurchaseStates.description)
@reset_text_handler
async def process_description(message: types.Message, state: FSMContext):
    await state.update_data(
        description=message.text
    )
    await FinanceBotInterface().add_purchase(
        purchase_data=await state.get_data(),
        message=message
    )
    await state.finish()
