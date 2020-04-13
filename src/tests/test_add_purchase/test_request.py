from src.domains.purchase import PurchaseDomain
from src.tests.base import BaseTestCase
from src.use_cases.add_purchase import AddPurchaseRequest


class TestRequestAddPurchaseTestCase(BaseTestCase):

    def test_valid_request(self):
        """ Тестирование валидного запроса """

        domain_purchase = PurchaseDomain(
            amount=100, description='Test', category='Test'
        )
        request = AddPurchaseRequest(
            purchase=domain_purchase
        )
        self.assertTrue(bool(request.is_valid()))
        self.assertEqual(domain_purchase, request.purchase)
