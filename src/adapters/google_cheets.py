from typing import Optional, List

from gspread import Cell
from gspread_asyncio import (
    AsyncioGspreadClient,
    AsyncioGspreadClientManager,
    AsyncioGspreadWorksheet,
    AsyncioGspreadSpreadsheet
)
from oauth2client.service_account import ServiceAccountCredentials

from libs.date import get_today_month


class GoogleSheetAdapter:
    """ """

    __sheet_url__: str = None
    __sheet__: Optional[AsyncioGspreadSpreadsheet] = None
    __client__: Optional[AsyncioGspreadClient] = None
    __credentials__: Optional[ServiceAccountCredentials] = None

    __now_month__: Optional[str] = None

    def __init__(
            self,
            url: str,
            credentials: ServiceAccountCredentials
    ):
        self.__sheet_url__ = url
        self.__credentials__ = credentials

    @property
    async def client(self) -> AsyncioGspreadClient:
        def credentials_wrap():
            return self.__credentials__

        if not self.__client__:
            client_manager = AsyncioGspreadClientManager(credentials_wrap)
            self.__client__ = await client_manager.authorize()
        return self.__client__

    @property
    async def sheet(self) -> AsyncioGspreadSpreadsheet:
        if not self.__sheet__:
            client = await self.client
            self.__sheet__ = await client.open_by_url(self.__sheet_url__)
        return self.__sheet__

    @property
    def now_month(self):
        if not self.__now_month__:
            self.__now_month__ = get_today_month()

        return self.__now_month__

    async def get_sheet_by_month(self, month: str) -> AsyncioGspreadWorksheet:
        sheet = await self.sheet
        return await sheet.worksheet(month)

    async def update_record(self, sheet_cells: List[Cell]) -> dict:
        worksheet = await self.get_sheet_by_month(self.now_month)
        return await worksheet.update_cells(cell_list=sheet_cells)
