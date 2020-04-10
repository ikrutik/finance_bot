import os
from enum import Enum
from typing import Optional, List, Dict


class StartupMode(Enum):
    WEBHOOK = 'webhook'
    POOLING = 'pooling'


PROJECT_ROOT: str = os.path.abspath(os.path.join(__file__, "../../../../"))
SRC_ROOT: str = os.path.abspath(os.path.join(PROJECT_ROOT, "src"))

# Параметры запуска приложения
HOST: str = "127.0.0.1"
PORT: int = 8081
DEBUG: bool = False

SSL_CONTEXT: Optional[tuple] = None
SKIP_UPDATES: bool = True
RELAX_TIMEOUT: float = 1.0

WEBHOOK_HOST: str = str()
WEBHOOK_PATH: str = str()
WEBHOOK_URL: str = str()

TELEGRAM_TOKEN: str = str()

GOOGLE_CLIENT_ID: str = str()
GOOGLE_CLIENT_SECRET: str = str()

COLUMN_INDEX_DESCRIPTION: int = 8
COLUMN_INDEX_AMOUNT: int = 9
COLUMN_INDEX_BUDGET_TODAY: int = 10
COLUMN_INDEX_BALANCE_TODAY: int = 11
COLUMN_INDEX_CATEGORY: int = 12

ROW_HEADER_OFFSET: int = 1

sheet_url: str = str()
scopes: List[str] = list()
credentials: Dict[str, str] = dict()

try:
    from .local_settings import *  # noqa
except ImportError:
    pass
