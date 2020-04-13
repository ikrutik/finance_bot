from src.tests.base import BaseTestCase
from src.use_cases.get_today_balance import GetTodayBalanceRequest


class TestRequestGetTodayBalanceTestCase(BaseTestCase):

    def test_valid_request(self):
        """ Тестирование валидного запроса """

        request = GetTodayBalanceRequest()
        self.assertTrue(bool(request.is_valid()))
