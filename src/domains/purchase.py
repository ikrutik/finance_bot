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
    """ Purchase Domain Model """

    amount: int
    description: str = str()
    category: str = str()

    def to_cells(self, row_index: int) -> List[Cell]:
        """
        Generate cells for update from model
        :param row_index: Row index in sheet
        """
        cell_amount = Cell(row=row_index, col=COLUMN_INDEX_AMOUNT, value=self.amount)
        cell_description = Cell(row=row_index, col=COLUMN_INDEX_DESCRIPTION, value=self.description)
        cell_category = Cell(row=row_index, col=COLUMN_INDEX_CATEGORY, value=self.category)

        return [cell_amount, cell_description, cell_category]

    @classmethod
    def from_dict(cls, data: dict) -> 'PurchaseDomain':
        """
        Create model from dict
        :param data: data
        """
        return cls(
            amount=data.get('amount', str()) or str(),
            category=data.get('category', str()) or str(),
            description=data.get('description', str()) or str()
        )
