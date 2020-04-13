from typing import Any, Optional

import aiogram.utils.markdown as md
from aiogram import types
from aiogram.types import ParseMode

from src.adapters.google_cheets import GoogleSheetAdapter
from src.base.use_case import BaseUseCaseResponse
from src.domains.purchase import PurchaseDomain
from src.libs import keyboard
from src.libs.helpers import load_credentials
from src.rest.applications.aiogram.bootstrap import get_dispatcher
from src.rest.settings import settings
from src.use_cases.add_purchase import (
    AddPurchaseRequest,
    AddPurchaseUseCase,
    AddPurchaseResponse
)
from src.use_cases.get_today_balance import (
    GetTodayBalanceResponse,
    GetTodayBalanceUseCase,
    GetTodayBalanceRequest
)
from src.use_cases.get_today_purchases import (
    GetTodayPurchasesResponse,
    GetTodayPurchasesRequest,
    GetTodayPurchasesUseCase
)


class FinanceBotInterface:
    """Interface for UseCases"""

    def __init__(self):
        self.dispatcher = get_dispatcher()

        self.sheet_adapter = GoogleSheetAdapter(
            url=settings.SHEET_URL,
            credentials=load_credentials(
                scopes=settings.AVAILABLE_GOOGLE_SCOPES,
                credentials=settings.GOOGLE_CREDENTIALS
            )
        )

    async def add_purchase(self, purchase_data: dict, message: types.Message):
        """
        Insert new purchase to sheet
        :param purchase_data: data for purchase
        :param message: telegram message
        """
        request: AddPurchaseRequest = AddPurchaseRequest(
            purchase=PurchaseDomain.from_dict(purchase_data)
        )
        use_case: AddPurchaseUseCase = AddPurchaseUseCase(
            sheet_adapter=self.sheet_adapter
        )
        response: AddPurchaseResponse = await use_case.execute(request)

        if bool(response):

            await self.dispatcher.bot.send_message(
                chat_id=message.chat.id,
                text=self.__get_response_text(success_value=response.balance_today),
                parse_mode=ParseMode.MARKDOWN_V2,
                reply_markup=keyboard.keyboard_menu
            )
        else:
            await self.dispatcher.bot.send_message(
                chat_id=message.chat.id,
                text=self.__get_response_text(failed_response=response),
                parse_mode=ParseMode.MARKDOWN_V2,
                reply_markup=keyboard.keyboard_menu
            )

    async def get_today_balance(self, message: types.Message):
        """
        Get balance of today from sheet
        :param message: telegram message
        """
        request: GetTodayBalanceRequest = GetTodayBalanceRequest()
        use_case: GetTodayBalanceUseCase = GetTodayBalanceUseCase(
            sheet_adapter=self.sheet_adapter
        )
        response: GetTodayBalanceResponse = await use_case.execute(request)

        if bool(response):
            await self.dispatcher.bot.send_message(
                chat_id=message.chat.id,
                text=self.__get_response_text(success_value=response.balance_today),
                parse_mode=ParseMode.MARKDOWN_V2,
                reply_markup=keyboard.keyboard_menu
            )
        else:
            await self.dispatcher.bot.send_message(
                chat_id=message.chat.id,
                text=self.__get_response_text(failed_response=response),
                parse_mode=ParseMode.MARKDOWN_V2,
                reply_markup=keyboard.keyboard_menu
            )

    async def get_today_purchases(self, message: types.Message):
        """
        Get today today_purchases from sheet
        :param message: telegram message
        """
        request: GetTodayPurchasesRequest = GetTodayPurchasesRequest()
        use_case: GetTodayPurchasesUseCase = GetTodayPurchasesUseCase(
            sheet_adapter=self.sheet_adapter
        )
        response: GetTodayPurchasesResponse = await use_case.execute(request)

        if bool(response):
            await self.dispatcher.bot.send_message(
                chat_id=message.chat.id,
                text=response.purchases,
                parse_mode=ParseMode.MARKDOWN_V2,
                reply_markup=keyboard.keyboard_menu
            )
        else:
            await self.dispatcher.bot.send_message(
                chat_id=message.chat.id,
                text=self.__get_response_text(failed_response=response),
                parse_mode=ParseMode.MARKDOWN_V2,
                reply_markup=keyboard.keyboard_menu
            )

    @classmethod
    def __get_response_text(
            cls,
            success_value: Optional[Any] = None,
            failed_response: Optional[BaseUseCaseResponse] = None) -> str:
        """
        Get text for response
        :param success_value: value for MD message
        :param failed_response: InvalidResponse
        """
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
