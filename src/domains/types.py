from enum import Enum

import aiogram.utils.markdown as md


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
    md.text('/add \- Добавление покупки'),  # NOQA
    md.text('/today \- Остаток на сегодня'),  # NOQA
    md.text('/month \- Остаток на месяц'),  # NOQA
    md.text('/purchase \- Показать покупки'),  # NOQA
    md.text('/help \- Помощь'),
    sep='\n',
)
