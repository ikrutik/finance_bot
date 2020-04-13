from unittest import mock

from src.adapters.google_cheets import GoogleSheetAdapter
from src.base.exception import PurchasesParseError
from src.rest.settings.settings import COLUMN_INDEX_AMOUNT, COLUMN_INDEX_DESCRIPTION
from src.tests.base import BaseTestCase
from src.use_cases.get_today_purchases import GetTodayPurchasesRequest, GetTodayPurchasesUseCase


class GetTodayPurchasesTestCase(BaseTestCase):

    async def asyncSetUp(self):
        self.sheet_adapter = GoogleSheetAdapter(
            url=str(), credentials=None
        )

    async def test_success_use_case_execute(self):
        amount = "500"
        purchases = "Bread, Sausages"
        row_values = [i for i in range(15)]
        row_values[COLUMN_INDEX_AMOUNT - 1] = amount
        row_values[COLUMN_INDEX_DESCRIPTION - 1] = purchases

        p = mock.patch(
            'src.tests.base.GoogleSheetAdapter.get_row_values',
            create=True, new=mock.AsyncMock(return_value=row_values)
        )
        self.addCleanup(p.stop)
        p.start()

        request: GetTodayPurchasesRequest = GetTodayPurchasesRequest()
        use_case: GetTodayPurchasesUseCase = GetTodayPurchasesUseCase(
            sheet_adapter=self.sheet_adapter
        )
        response = await use_case.execute(request)

        self.assertIn(amount, response.value.get('response'))
        for p in purchases.split(','):
            self.assertIn(p, response.value.get('response'))

    async def test_failed_use_case_execute_if_row_values_is_empty(self):
        p = mock.patch(
            'src.tests.base.GoogleSheetAdapter.get_row_values',
            create=True, new=mock.AsyncMock(return_value=list())
        )
        self.addCleanup(p.stop)
        p.start()

        request: GetTodayPurchasesRequest = GetTodayPurchasesRequest()
        use_case: GetTodayPurchasesUseCase = GetTodayPurchasesUseCase(
            sheet_adapter=self.sheet_adapter
        )

        response = await use_case.execute(request)
        self.assertIsInstance(response.errors[0], PurchasesParseError)
