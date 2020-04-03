from dataclasses import dataclass
from typing import List

from gspread import Cell

from rest.settings.settings import (
    COLUMN_INDEX_DESCRIPTION,
    COLUMN_INDEX_CATEGORY,
    COLUMN_INDEX_AMOUNT
)


@dataclass
class PurchaseDomain:
    amount: int
    description: str = str()
    category: str = str()

    def to_cells(self, row_index: int) -> List[Cell]:
        cell_amount = Cell(row=row_index, col=COLUMN_INDEX_AMOUNT, value=self.amount)
        cell_description = Cell(row=row_index, col=COLUMN_INDEX_DESCRIPTION, value=self.description)
        cell_category = Cell(row=row_index, col=COLUMN_INDEX_CATEGORY, value=self.category)
        return [cell_amount, cell_description, cell_category]
