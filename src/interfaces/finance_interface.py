from aiogram import types
from aiogram.types import ReplyKeyboardRemove

from adapters.google_cheets import GoogleSheetAdapter
from domains.purchase import PurchaseDomain
from libs import keyboard
from libs.helpers import load_credentials
from rest.settings import settings
from use_cases.add_purchase import AddPurchaseRequest, AddPurchaseUseCase, AddPurchaseResponse


class FinanceBotInterface:

    def __init__(self):
        self.sheet_adapter = GoogleSheetAdapter(
            url=settings.sheet_url,
            credentials=load_credentials(
                scopes=settings.scopes,
                credentials=settings.credentials
            )
        )

    async def add_purchase(self, purchase_data: dict, message: types.Message):
        request: AddPurchaseRequest = AddPurchaseRequest(
            purchase=PurchaseDomain.from_dict(purchase_data)
        )
        use_case: AddPurchaseUseCase = AddPurchaseUseCase(
            sheet_adapter=self.sheet_adapter
        )
        response: AddPurchaseResponse = await use_case.execute(request)

        if bool(response):
            await message.reply(
                text=f'Запись успешно добавлена, осталось на день: {response.balance_today} руб.',
                reply_markup=ReplyKeyboardRemove()
            )
            await message.reply(
                text='Теперь можете добавить новую покупку',
                reply_markup=keyboard.keyboard_menu
            )
        else:
            await message.reply(
                text=f'Произошла ошибка {response.get_first_error_message()}',
                reply_markup=ReplyKeyboardRemove()
            )
            await message.reply(
                text='Повторите добавление покупки',
                reply_markup=keyboard.keyboard_menu
            )

    async def get_today_balance(self, message: types.Message):
        pass

    async def get_month_balance(self, message: types.Message):
        pass
