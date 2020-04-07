from enum import Enum

import aiogram.utils.markdown as md
from aiogram.utils.helper import Helper, HelperMode, ListItem


class PurchaseCategory(Enum):
    """ """

    MEAL = 'Еда'


class TestStates(Helper):
    """ """

    mode = HelperMode.snake_case

    TEST_STATE_0 = ListItem()
    TEST_STATE_1 = ListItem()
    TEST_STATE_2 = ListItem()
    TEST_STATE_3 = ListItem()
    TEST_STATE_4 = ListItem()
    TEST_STATE_5 = ListItem()


TestStates.all()

HELP_DESCRIPTION = md.text(
    md.text('C помощью бота вы сможете:', ),
    md.text('Добавить покупку'),
    md.text('Узнать остаток'),
    md.text('Посмотреь свои покупки'),
    md.text(''),
    md.text('Основные команды:'),
    md.text('/add \- Добавление покупки'),
    md.text('/today \- Остаток на сегодня'),
    md.text('/month \- Остаток на месяц'),
    md.text('/purchase \- Показать покупки'),
    md.text('/help \- Помощь'),
    sep='\n',
)
