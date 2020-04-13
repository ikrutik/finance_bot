from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    KeyboardButton
)

from src.domains.types import PurchaseCategory

# RESET BUTTON
button_reset = KeyboardButton(PurchaseCategory.RESET.value)

# MENU KEYBOARD
keyboard_menu = InlineKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).row(
    InlineKeyboardButton('Добавить', callback_data='add'),
    InlineKeyboardButton('Баланс', callback_data='balance'),
    InlineKeyboardButton('Покупки', callback_data='purchases'),
    InlineKeyboardButton('Сброс', callback_data='reset'),
)

# CATEGORIES KEYBOARD
keyboard_categories = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).row(
    KeyboardButton(PurchaseCategory.MEAL.value),
    KeyboardButton(PurchaseCategory.REST.value),
    KeyboardButton(PurchaseCategory.CAR.value),
    KeyboardButton(PurchaseCategory.EDUCATION.value),
).insert(
    button_reset
)

# AMOUNT KEYBOARD
keyboard_amount = ReplyKeyboardMarkup(
    one_time_keyboard=True, resize_keyboard=True
).row(
    KeyboardButton('50'), KeyboardButton('150'), KeyboardButton('300'),
    KeyboardButton('500'), KeyboardButton('700'), KeyboardButton('1000')
).insert(
    button_reset
)

# DESCRIPTION KEYBOARD
keyboard_description = ReplyKeyboardMarkup(
    one_time_keyboard=True, resize_keyboard=True
).row(
    KeyboardButton('Потом дописать'), button_reset
)
