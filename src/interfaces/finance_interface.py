from typing import Any, Optional

import aiogram.utils.markdown as md
from aiogram import types
from aiogram.types import ParseMode

from adapters.google_cheets import GoogleSheetAdapter
from base.use_case import BaseUseCaseResponse
from domains.purchase import PurchaseDomain
from libs import keyboard
from libs.helpers import load_credentials
from rest.settings import settings
from use_cases.add_purchase import AddPurchaseRequest, AddPurchaseUseCase, AddPurchaseResponse
from use_cases.get_today_balance import GetTodayBalanceResponse, GetTodayBalanceUseCase, GetTodayBalanceRequest
from use_cases.get_today_purchases import GetTodayPurchasesResponse, GetTodayPurchasesRequest, GetTodayPurchasesUseCase


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
                text=self.__get_response_text(success_value=response.balance_today),
                parse_mode=ParseMode.MARKDOWN_V2,
                reply_markup=keyboard.keyboard_menu
            )
        else:
            await message.reply(
                text=self.__get_response_text(failed_response=response),
                parse_mode=ParseMode.MARKDOWN_V2,
                reply_markup=keyboard.keyboard_menu,
            )

    async def get_today_balance(self, message: types.Message):
        request: GetTodayBalanceRequest = GetTodayBalanceRequest()
        use_case: GetTodayBalanceUseCase = GetTodayBalanceUseCase(
            sheet_adapter=self.sheet_adapter
        )
        response: GetTodayBalanceResponse = await use_case.execute(request)

        if bool(response):
            await message.reply(
                text=self.__get_response_text(success_value=response.balance_today),
                parse_mode=ParseMode.MARKDOWN_V2,
                reply_markup=keyboard.keyboard_menu
            )
        else:
            await message.reply(
                text=self.__get_response_text(failed_response=response),
                parse_mode=ParseMode.MARKDOWN_V2,
                reply_markup=keyboard.keyboard_menu,
            )

    async def get_today_purchases(self, message: types.Message):
        request: GetTodayPurchasesRequest = GetTodayPurchasesRequest()
        use_case: GetTodayPurchasesUseCase = GetTodayPurchasesUseCase(
            sheet_adapter=self.sheet_adapter
        )
        response: GetTodayPurchasesResponse = await use_case.execute(request)

        if bool(response):
            await message.reply(
                text=response.purchases,
                reply_markup=keyboard.keyboard_menu
            )
        else:
            await message.reply(
                text=self.__get_response_text(failed_response=response),
                parse_mode=ParseMode.MARKDOWN_V2,
                reply_markup=keyboard.keyboard_menu,
            )

    @classmethod
    def __get_response_text(
            cls,
            success_value: Optional[Any] = None,
            failed_response: Optional[BaseUseCaseResponse] = None) -> str:

        if success_value:
            return md.text(
                md.text("💥Осталось на день: "),
                md.bold(f"{success_value} руб"),
                sep=" ",
            )
        elif failed_response is not None:
            return md.text(
                md.text("🔥Произошла ошибка: "),
                md.bold(f"{failed_response.get_first_error_message()}"),
                sep=" ",
            )

        return md.text(str())
