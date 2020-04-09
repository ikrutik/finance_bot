from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

from domains.types import PurchaseCategory

keyboard_menu = InlineKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).row(
    InlineKeyboardButton('Добавить', callback_data='add'),
    InlineKeyboardButton('Баланс', callback_data='balance'),
    InlineKeyboardButton('Покупки', callback_data='purchases'),
    InlineKeyboardButton('Сброс', callback_data='reset'),
)

button_category_1 = KeyboardButton(PurchaseCategory.MEAL.value)
button_category_2 = KeyboardButton(PurchaseCategory.REST.value)
button_category_3 = KeyboardButton(PurchaseCategory.CAR.value)
button_category_4 = KeyboardButton(PurchaseCategory.EDUCATION.value)
button_reset = KeyboardButton(PurchaseCategory.RESET.value)

keyboard_categories = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).row(
    button_category_1,
    button_category_2,
    button_category_3,
    button_category_4,
).insert(
    button_reset
)

keyboard_amount = ReplyKeyboardMarkup(
    one_time_keyboard=True, resize_keyboard=True
).row(
    KeyboardButton('50'), KeyboardButton('150'), KeyboardButton('300'),
    KeyboardButton('500'), KeyboardButton('700'), KeyboardButton('1000')
).insert(
    button_reset
)

keyboard_description = ReplyKeyboardMarkup(
    one_time_keyboard=True, resize_keyboard=True
).row(
    KeyboardButton('Потом дописать'),
    button_reset
)


class PurchaseStates(StatesGroup):
    category = State()
    amount = State()
    description = State()