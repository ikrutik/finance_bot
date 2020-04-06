import asyncio
from typing import Tuple, Optional

from aiogram import types

from base.use_case import BaseUseCaseResponse, BaseUseCaseRequest, BaseUseCase
from domains.purchase import PurchaseDomain


class AddPurchaseRequest(BaseUseCaseRequest):
    def __init__(self, message: types.Message):
        super().__init__()
        self.message = message

    def is_valid(self, *args, **kwargs):
        return self


class AddPurchaseResponse(BaseUseCaseResponse):
    pass


class AddPurchaseUseCase(BaseUseCase):
    async def __execute__(self, request: AddPurchaseRequest, *args, **kwargs) -> AddPurchaseResponse:
        amount, description, category = self.get_purchase_data(text=request.message.text)
        purchase = PurchaseDomain(amount=amount, description=description, category=category)
        await asyncio.create_task(self.sheet_adapter.update_record(purchase.to_cells(row_index=11)))
        return AddPurchaseResponse(value=amount)

    def get_purchase_data(self, text: str) -> Tuple[int, str, str]:
        """

        :param text:
        """

        category = description = str()

        split_text = list()
        for word in text.split(" "):
            if '/' in word:
                continue
            if word in ["", "'"]:
                continue
            split_text.append(word)

        if len(split_text) == 3:
            amount, description, category = split_text
        elif len(split_text) == 2:
            amount, description = split_text
        elif len(split_text) == 1:
            amount = split_text[0]
        else:
            raise Exception()

        try:

            amount = int(amount)
            description = str(description)
            category = str(category)

        except ValueError:
            raise Exception()

        return amount, description, category
