from unittest import mock

from src.base.exception import BalanceParseError
from src.rest.settings.settings import COLUMN_INDEX_BALANCE_TODAY
from src.tests.base import BaseTestCase
from src.use_cases.get_today_balance import GetTodayBalanceUseCase, GetTodayBalanceRequest


class GetTodayBalanceTestCase(BaseTestCase):

    async def test_success_use_case_execute(self):
        balance = "1000"
        row_values = [i for i in range(15)]
        row_values[COLUMN_INDEX_BALANCE_TODAY - 1] = balance

        p = mock.patch(
            'src.tests.base.GoogleSheetAdapter.get_row_values',
            create=True, new=mock.AsyncMock(return_value=row_values)
        )
        self.addCleanup(p.stop)
        p.start()

        request: GetTodayBalanceRequest = GetTodayBalanceRequest()
        use_case: GetTodayBalanceUseCase = GetTodayBalanceUseCase(
            sheet_adapter=self.sheet_adapter
        )
        response = await use_case.execute(request)

        self.assertEqual(response.value.get('response'), int(balance))

    async def test_failed_use_case_execute_if_row_values_is_empty(self):
        p = mock.patch(
            'src.tests.base.GoogleSheetAdapter.get_row_values',
            create=True, new=mock.AsyncMock(return_value=list())
        )
        self.addCleanup(p.stop)
        p.start()

        request: GetTodayBalanceRequest = GetTodayBalanceRequest()
        use_case: GetTodayBalanceUseCase = GetTodayBalanceUseCase(
            sheet_adapter=self.sheet_adapter
        )
        response = await use_case.execute(request)

        self.assertIsInstance(response.errors[0], BalanceParseError)
