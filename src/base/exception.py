from dataclasses import dataclass


@dataclass
class BaseFinanceException(Exception):
    error_code: int = 50000
    http_code: int = 500
    message: str = "Base finance error"
