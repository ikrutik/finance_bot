from datetime import datetime

from adapters.google_cheets import GoogleSheetAdapter
from base.use_case import BaseUseCase, BaseUseCaseRequest, BaseUseCaseResponse
from rest.settings.settings import ROW_HEADER_OFFSET


class BaseFinanceUseCase(BaseUseCase):
    def __init__(
            self,
            sheet_adapter: GoogleSheetAdapter
    ):
        self.sheet_adapter = sheet_adapter

    async def __execute__(self, request: BaseUseCaseRequest, *args, **kwargs) -> BaseUseCaseResponse:
        raise NotImplementedError()

    @classmethod
    def get_row_index_for_update(cls) -> int:
        """ """
        return datetime.today().day + ROW_HEADER_OFFSET
