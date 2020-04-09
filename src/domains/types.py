from enum import Enum

import aiogram.utils.markdown as md


class PurchaseCategory(Enum):
    """ """

    MEAL = 'Еда'
    REST = 'Отдых'
    CAR = 'Машина'
    EDUCATION = 'Образование'
    RESET = 'Сброс'


HELP_DESCRIPTION = md.text(
    md.bold('🔥C помощью бота вы сможете:', ),
    md.text('✅Добавить покупку'),
    md.text('✅Узнать остаток'),
    md.text('✅Посмотреь свои покупки'),
    md.text(''),
    md.bold('Основные команды:'),
    md.text('/add \- Добавление покупки'),
    md.text('/today \- Остаток на сегодня'),
    md.text('/month \- Остаток на месяц'),
    md.text('/purchase \- Показать покупки'),
    md.text('/help \- Помощь'),
    sep='\n',
)