"""
Use Case for get purchases
"""
from typing import List

import aiogram.utils.markdown as md

from src.base.exception import PurchasesParseError
from src.base.use_case import BaseUseCaseResponse, BaseUseCaseRequest
from src.rest.settings.settings import COLUMN_INDEX_DESCRIPTION, COLUMN_INDEX_AMOUNT
from src.use_cases.base_finance import BaseFinanceUseCase


class GetTodayPurchasesRequest(BaseUseCaseRequest):
    def __init__(self):
        super().__init__()

    def is_valid(self, *args, **kwargs):
        return self


class GetTodayPurchasesResponse(BaseUseCaseResponse):
    def __init__(self, purchases: str):
        super().__init__(value=dict(response=purchases))
        self.purchases = purchases


class GetTodayPurchasesUseCase(BaseFinanceUseCase):
    async def __execute__(self, request: GetTodayPurchasesRequest, *args, **kwargs) -> GetTodayPurchasesResponse:

        row_current_values = await self.sheet_adapter.get_row_values(
            row_index=self.get_row_index_for_update()
        )
        purchases = self.get_today_purchases(
            row_values=row_current_values
        )
        return GetTodayPurchasesResponse(purchases=purchases)

    @classmethod
    def get_today_purchases(cls, row_values: List[str]) -> str:
        """
        Get today purchases
        :param row_values: list of values from row
        :raise PurchasesParseError
        """

        try:
            description = row_values[COLUMN_INDEX_DESCRIPTION - 1].split(',')
            purchases = [s for s in description if s.strip()]

            if not purchases:
                return md.bold("👀Сегодня нет покупок")

            amount = int("".join(row_values[COLUMN_INDEX_AMOUNT - 1].split(',')) or 0)

            return md.text(
                md.bold(f"Сумма покупок: {amount}"),
                md.text(*purchases, sep='\n'),
                sep='\n'
            )

        except (IndexError, ValueError, AttributeError):
            raise PurchasesParseError()
