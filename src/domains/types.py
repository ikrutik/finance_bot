from enum import Enum

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
