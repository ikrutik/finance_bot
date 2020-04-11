from enum import Enum

import aiogram.utils.markdown as md
from aiogram.dispatcher.filters.state import StatesGroup, State


class PurchaseStates(StatesGroup):
    """ States purchase flow """

    category = State()
    amount = State()
    description = State()


class PurchaseCategory(Enum):
    """ Categories for purchase """

    MEAL = 'Еда'
    REST = 'Отдых'
    CAR = 'Машина'
    EDUCATION = 'Образование'
    RESET = 'Сброс'


# Description for /help command
HELP_DESCRIPTION = md.text(
    md.bold('🔥C помощью бота вы сможете:', ),
    md.text('✅Добавить покупку'),
    md.text('✅Узнать остаток'),
    md.text('✅Посмотреь свои покупки'),
    md.text(''),
    md.bold('Основные команды:'),
    md.text('/add \- Добавление покупки'),  # noqa
    md.text('/balance \- Остаток на сегодня'),  # noqa
    md.text('/purchases \- Показать покупки'),  # noqa
    md.text('/menu \- Показать меню'),  # noqa
    md.text('/reset \- Сброс'),  # noqa
    md.text('/help \- Помощь'),  # noqa
    sep='\n',
)
