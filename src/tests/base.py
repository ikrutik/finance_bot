from unittest import IsolatedAsyncioTestCase

from src.adapters.google_cheets import GoogleSheetAdapter


class BaseTestCase(IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.sheet_adapter = GoogleSheetAdapter(
            url=str(), credentials=None
        )
