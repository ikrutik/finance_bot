from typing import List

import aiogram.utils.markdown as md

from base.use_case import BaseUseCaseResponse, BaseUseCaseRequest
from rest.settings.settings import (
    COLUMN_INDEX_DESCRIPTION)
from use_cases.base_finance_use_case import BaseFinanceUseCase


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

        try:
            purchases = [s.strip() for s in row_values[COLUMN_INDEX_DESCRIPTION - 1].split(',')]
            return md.text(*purchases, sep='\n')

        except (IndexError, ValueError, AttributeError):
            raise Exception()
