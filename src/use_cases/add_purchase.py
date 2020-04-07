import asyncio
from datetime import datetime
from typing import List

from base.use_case import BaseUseCaseResponse, BaseUseCaseRequest, BaseUseCase
from domains.purchase import PurchaseDomain
from rest.settings.settings import (
    COLUMN_INDEX_DESCRIPTION,
    COLUMN_INDEX_CATEGORY,
    COLUMN_INDEX_AMOUNT,
    COLUMN_INDEX_BUDGET_TODAY,
    ROW_HEADER_OFFSET)


class AddPurchaseRequest(BaseUseCaseRequest):
    def __init__(self, purchase: PurchaseDomain):
        super().__init__()
        self.purchase = purchase

    def is_valid(self, *args, **kwargs):
        return self


class AddPurchaseResponse(BaseUseCaseResponse):
    def __init__(self, balance_today: int):
        super().__init__(value=dict(response=balance_today))
        self.balance_today = balance_today


class AddPurchaseUseCase(BaseUseCase):
    async def __execute__(self, request: AddPurchaseRequest, *args, **kwargs) -> AddPurchaseResponse:
        row_index_for_update = self.get_row_index_for_update()

        row_current_values = await self.sheet_adapter.get_row_values(
            row_index=row_index_for_update
        )
        purchase_to_update = self.get_purchase_with_current_values(
            purchase=request.purchase, row_values=row_current_values
        )
        balance_today = self.get_today_balance(
            purchase=purchase_to_update, row_values=row_current_values
        )
        purchase_cells = request.purchase.to_cells(
            row_index=row_index_for_update
        )
        task_for_execute = self.sheet_adapter.update_cells(
            sheet_cells=purchase_cells
        )

        await asyncio.create_task(task_for_execute)

        return AddPurchaseResponse(balance_today=balance_today)

    @classmethod
    def get_row_index_for_update(cls) -> int:
        """ """
        return datetime.today().day + ROW_HEADER_OFFSET

    def get_purchase_with_current_values(self, purchase: PurchaseDomain, row_values: List[str]) -> PurchaseDomain:

        try:
            current_amount = int("".join(row_values[COLUMN_INDEX_AMOUNT - 1].split(',')))
            purchase.amount += current_amount
        except (IndexError, ValueError, AttributeError):
            pass
        try:
            purchase.description = f"{purchase.description}, {row_values[COLUMN_INDEX_DESCRIPTION - 1]}"
        except IndexError:
            pass
        try:
            purchase.category = f"{purchase.category}, {row_values[COLUMN_INDEX_CATEGORY - 1]}"
        except IndexError:
            pass

        return purchase

    @classmethod
    def get_today_balance(cls, purchase: PurchaseDomain, row_values: List[str]) -> int:
        try:
            budget_today = int("".join(row_values[COLUMN_INDEX_BUDGET_TODAY - 1].split(',')))
            return budget_today - purchase.amount
        except (IndexError, ValueError, AttributeError):
            raise Exception()
