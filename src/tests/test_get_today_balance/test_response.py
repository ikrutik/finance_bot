from src.tests.base import BaseTestCase
from src.use_cases.get_today_balance import GetTodayBalanceResponse


class TestResponseGetTodayBalanceTestCase(BaseTestCase):

    def test_success_response(self):
        balance = 500
        response = GetTodayBalanceResponse(
            balance_today=balance
        )
        self.assertEqual(response.value.get('response'), balance)
