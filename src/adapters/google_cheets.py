from typing import Optional, List

from gspread import Cell, WorksheetNotFound
from gspread_asyncio import (
    AsyncioGspreadClient,
    AsyncioGspreadClientManager,
    AsyncioGspreadWorksheet,
    AsyncioGspreadSpreadsheet
)
from oauth2client.service_account import ServiceAccountCredentials

from base.exception import WorkSheetNotFoundError
from libs.date import get_now_month_name


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

    async def get_sheet_by_month(self, month_name: Optional[str] = None) -> AsyncioGspreadWorksheet:

        try:
            sheet = await self.sheet
            month = month_name or get_now_month_name()
            worksheet = await sheet.worksheet(month)
            return worksheet

        except WorksheetNotFound :
            raise WorkSheetNotFoundError()

    async def get_row_values(self, row_index: int, month_name: Optional[str] = None) -> dict:
        worksheet = await self.get_sheet_by_month(month_name=month_name)
        row_values = await worksheet.row_values(row_index)
        return row_values

    async def update_cells(self, sheet_cells: List[Cell], month_name: Optional[str] = None) -> dict:
        worksheet = await self.get_sheet_by_month(month_name=month_name)
        result = await worksheet.update_cells(cell_list=sheet_cells)
        return result
