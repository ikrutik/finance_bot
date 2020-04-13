from src.tests.base import BaseTestCase
from src.use_cases.get_today_purchases import GetTodayPurchasesRequest


class TestRequestGetTodayPurchaseTestCase(BaseTestCase):

    def test_valid_request(self):
        """ Тестирование валидного запроса """

        request = GetTodayPurchasesRequest()
        self.assertTrue(bool(request.is_valid()))
