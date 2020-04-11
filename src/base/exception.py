from typing import Optional


class BaseFinanceException(Exception):
    """
    Base exception for project
    """

    error_code: int = 50000
    http_code: int = 500
    message: str = "Base exception"

    def __init__(
            self,
            error_code: Optional[int] = None,
            http_code: Optional[int] = None,
            message: Optional[str] = None
    ):
        if error_code:
            self.error_code = error_code
        if http_code:
            self.http_code = http_code
        if message:
            self.message = message


class BalanceParseError(BaseFinanceException):
    error_code: int = 40010
    http_code: int = 400
    message: str = "Ошибка при парсинге баланса"


class PurchasesParseError(BaseFinanceException):
    error_code: int = 40015
    http_code: int = 400
    message: str = "Ошибка при парсинге покупок"


class PurchaseCreateError(BaseFinanceException):
    error_code: int = 40020
    http_code: int = 400
    message: str = "Ошибка при составлении покупки"


class WorkSheetNotFoundError(BaseFinanceException):
    error_code: int = 40410
    http_code: int = 404
    message: str = "Не найдена таблица при поиске"
