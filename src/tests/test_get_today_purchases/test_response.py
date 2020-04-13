from src.tests.base import BaseTestCase
from src.use_cases.get_today_purchases import GetTodayPurchasesResponse


class TestResponseGetTodayPurchaseTestCase(BaseTestCase):

    def test_success_response(self):
        """ Тестирование валидного ответа """

        purchases = """
            - Purchase 1
            - Purchase 2
        """
        response = GetTodayPurchasesResponse(
            purchases=purchases
        )
        self.assertEqual(response.value.get('response'), purchases)
