from aiogram import types

from adapters.google_cheets import GoogleSheetAdapter
from base.use_case import BaseUseCaseResponse
from libs.helpers import load_credentials
from rest.settings import settings
from use_cases.add_purchase import AddPurchaseRequest, AddPurchaseUseCase


async def serialize(message: types.Message, response: BaseUseCaseResponse):
    if bool(response):
        return await message.reply(response.value)
    else:
        return message.reply(next((str(e) for e in response.errors), 'Exception'))


class FinanceBotInterface:

    def __init__(self):
        self.sheet_adapter = GoogleSheetAdapter(
            url=settings.sheet_url,
            credentials=load_credentials(
                scopes=settings.scopes,
                credentials=settings.credentials
            )
        )

    async def add_purchase(self, message: types.Message):
        request = AddPurchaseRequest(
            message=message
        )
        use_case = AddPurchaseUseCase(
            sheet_adapter=self.sheet_adapter
        )
        response = await use_case.execute(request)
        return await serialize(message, response)

    async def get_today_balance(self, message: types.Message):
        pass

    async def get_month_balance(self, message: types.Message):
        pass
