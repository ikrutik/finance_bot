"""
Use Case for get balance
"""
from typing import List

from base.exception import BalanceParseError
from base.use_case import BaseUseCaseResponse, BaseUseCaseRequest
from rest.settings.settings import COLUMN_INDEX_BALANCE_TODAY
from use_cases.base_finance import BaseFinanceUseCase


class GetTodayBalanceRequest(BaseUseCaseRequest):
    def __init__(self):
        super().__init__()

    def is_valid(self, *args, **kwargs):
        return self


class GetTodayBalanceResponse(BaseUseCaseResponse):
    def __init__(self, balance_today: int):
        super().__init__(value=dict(response=balance_today))
        self.balance_today = balance_today


class GetTodayBalanceUseCase(BaseFinanceUseCase):
    async def __execute__(self, request: GetTodayBalanceRequest, *args, **kwargs) -> GetTodayBalanceResponse:

        row_current_values = await self.sheet_adapter.get_row_values(
            row_index=self.get_row_index_for_update()
        )
        balance_today = self.get_today_balance(
            row_values=row_current_values
        )
        return GetTodayBalanceResponse(balance_today=balance_today)

    @classmethod
    def get_today_balance(cls, row_values: List[str]) -> int:
        """
        Get today balance
        :param row_values: list of values from row
        :raise BalanceParseError
        """

        try:
            balance_today = int("".join(row_values[COLUMN_INDEX_BALANCE_TODAY - 1].split(',')))
            return balance_today

        except (IndexError, ValueError, AttributeError):
            raise BalanceParseError()
