from unittest import mock

from src.base.exception import PurchaseCreateError, BalanceParseError
from src.domains.purchase import PurchaseDomain
from src.rest.settings.settings import (
    COLUMN_INDEX_BALANCE_TODAY,
    COLUMN_INDEX_AMOUNT,
    COLUMN_INDEX_DESCRIPTION,
    COLUMN_INDEX_CATEGORY,
    COLUMN_INDEX_BUDGET_TODAY
)
from src.tests.base import BaseTestCase
from src.use_cases.add_purchase import AddPurchaseRequest, AddPurchaseUseCase


class AddPurchaseTestCase(BaseTestCase):

    async def test_success_use_case_execute(self):
        amount = "1,000"
        balance = "2,597"
        budget_today = "3,597"

        category = "Test"
        description = "Test"

        # Return row_values
        row_values = [i for i in range(15)]

        row_values[COLUMN_INDEX_AMOUNT - 1] = amount
        row_values[COLUMN_INDEX_BALANCE_TODAY - 1] = balance
        row_values[COLUMN_INDEX_DESCRIPTION - 1] = description
        row_values[COLUMN_INDEX_CATEGORY - 1] = category
        row_values[COLUMN_INDEX_BUDGET_TODAY - 1] = budget_today

        p1 = mock.patch(
            'src.tests.base.GoogleSheetAdapter.get_row_values',
            create=True, new=mock.AsyncMock(return_value=row_values)
        )
        p2 = mock.patch(
            'src.tests.base.GoogleSheetAdapter.update_cells',
            create=True, new=mock.AsyncMock(return_value=())
        )
        self.addCleanup(p1.stop)
        self.addCleanup(p2.stop)

        p1.start()
        p2.start()

        purchase_amount = 300
        domain_purchase = PurchaseDomain(
            amount=purchase_amount,
            description='Test',
            category='Test'
        )
        request: AddPurchaseRequest = AddPurchaseRequest(
            purchase=domain_purchase
        )
        use_case: AddPurchaseUseCase = AddPurchaseUseCase(
            sheet_adapter=self.sheet_adapter
        )
        response = await use_case.execute(request)

        balance_today = int("".join(balance.split(','))) - purchase_amount
        self.assertEqual(response.value.get('response'), balance_today)

    async def test_failed_use_case_execute_if_row_values_is_empty(self):
        p = mock.patch(
            'src.tests.base.GoogleSheetAdapter.get_row_values',
            create=True, new=mock.AsyncMock(return_value=list())
        )
        self.addCleanup(p.stop)
        p.start()

        domain_purchase = PurchaseDomain(
            amount=1000,
            description='Test',
            category='Test'
        )
        request: AddPurchaseRequest = AddPurchaseRequest(
            purchase=domain_purchase
        )
        use_case: AddPurchaseUseCase = AddPurchaseUseCase(
            sheet_adapter=self.sheet_adapter
        )
        response = await use_case.execute(request)

        self.assertIsInstance(response.errors[0], PurchaseCreateError)

    async def test_failed_use_case_execute_if_budget_today_invalid(self):
        amount = "1,000"
        balance = "2,597"
        category = "Test"
        description = "Test"

        budget_today = "Invalid values"

        # Return row_values
        row_values = [i for i in range(15)]

        row_values[COLUMN_INDEX_AMOUNT - 1] = amount
        row_values[COLUMN_INDEX_BALANCE_TODAY - 1] = balance
        row_values[COLUMN_INDEX_DESCRIPTION - 1] = description
        row_values[COLUMN_INDEX_CATEGORY - 1] = category
        row_values[COLUMN_INDEX_BUDGET_TODAY - 1] = budget_today

        p = mock.patch(
            'src.tests.base.GoogleSheetAdapter.get_row_values',
            create=True, new=mock.AsyncMock(return_value=row_values)
        )
        self.addCleanup(p.stop)
        p.start()

        domain_purchase = PurchaseDomain(
            amount=1000,
            description='Test',
            category='Test'
        )
        request: AddPurchaseRequest = AddPurchaseRequest(
            purchase=domain_purchase
        )
        use_case: AddPurchaseUseCase = AddPurchaseUseCase(
            sheet_adapter=self.sheet_adapter
        )
        response = await use_case.execute(request)

        self.assertIsInstance(response.errors[0], BalanceParseError)
