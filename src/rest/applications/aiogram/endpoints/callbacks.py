from aiogram import types

from libs import keyboard
from libs.keyboard import PurchaseStates
from rest.applications.aiogram.bootstrap import get_dispatcher

dispatcher = get_dispatcher()


@dispatcher.callback_query_handler(lambda c: c.data and c.data == 'add')
async def process_callback_add(callback_query: types.CallbackQuery):
    """ """

    await dispatcher.bot.answer_callback_query(callback_query.id)
    await PurchaseStates.category.set()
    await callback_query.message.reply(
        text="Выберите категорию",
        reply_markup=keyboard.keyboard_categories)


@dispatcher.callback_query_handler(lambda c: c.data and 'category' == c.data.split('.')[0])
async def process_category(callback_query: types.CallbackQuery):
    """ """

    category_name = callback_query.data.split('.')[1]
    await dispatcher.bot.answer_callback_query(callback_query.id)
    # await dispatcher.bot.edit_message_text(
    #     text=f'Теперь запишите сумму покупки для категории {category_name}',
    #     chat_id=callback_query.from_user.id
    # )
    await callback_query.message.edit_text(
        text=f'Теперь запишите сумму покупки для категории {category_name}',
        reply_markup=keyboard.keyboard_amount
    )

    # await dispatcher.bot.send_message(
    #     chat_id=callback_query.from_user.id,
    #     text=f'Теперь запишите сумму покупки для категории {category_name}',
    #     reply_markup=keyboard.keyboard_amount
    # )


@dispatcher.callback_query_handler(lambda c: c.data and c.data == 'amount')
async def process_category(callback_query: types.CallbackQuery):
    """ """

    await dispatcher.bot.answer_callback_query(callback_query.id)
    await dispatcher.bot.send_message(
        chat_id=callback_query.from_user.id,
        text=f'Теперь запишите описание',
    )
