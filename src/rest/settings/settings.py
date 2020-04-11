import logging
import os
from enum import Enum
from typing import Optional, List, Dict

PROJECT_ROOT: str = os.path.abspath(os.path.join(__file__, "../../../../"))
SRC_ROOT: str = os.path.abspath(os.path.join(PROJECT_ROOT, "src"))

# Logging
BASE_LOG_LEVEL = logging.DEBUG

# Running params
HOST: str = "127.0.0.1"
PORT: int = 8081
DEBUG: bool = False
SSL_CONTEXT: Optional[tuple] = None
SKIP_UPDATES: bool = True
RELAX_TIMEOUT: float = 1.0

# Webhook setting
WEBHOOK_HOST: str = str()
WEBHOOK_PATH: str = str()
WEBHOOK_URL: str = str()

# Bot token
TELEGRAM_BOT_TOKEN: str = str()

# Google credentials
SHEET_URL: str = str()

GOOGLE_CLIENT_ID: str = str()
GOOGLE_CLIENT_SECRET: str = str()
AVAILABLE_GOOGLE_SCOPES: List[str] = list()
GOOGLE_CREDENTIALS: Dict[str, str] = dict()

# Indexes of sheet
ROW_HEADER_OFFSET: int = 1

COLUMN_INDEX_DESCRIPTION: int = 8
COLUMN_INDEX_AMOUNT: int = 9
COLUMN_INDEX_BUDGET_TODAY: int = 10
COLUMN_INDEX_BALANCE_TODAY: int = 11
COLUMN_INDEX_CATEGORY: int = 12


# Mode for startup bot
class StartupMode(Enum):
    WEBHOOK = 'webhook'
    POOLING = 'pooling'


# Import local settings
try:
    from .local_settings import *  # noqa
except ImportError:
    pass
