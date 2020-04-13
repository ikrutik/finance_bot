from src.tests.base import BaseTestCase
from src.use_cases.add_purchase import AddPurchaseResponse


class TestResponseAddPurchaseTestCase(BaseTestCase):

    def test_success_response(self):
        balance = 500
        response = AddPurchaseResponse(
            balance_today=balance
        )
        self.assertEqual(response.value.get('response'), balance)
