from .EqualExpenseStrategy import EqualExpenseStrategy
from .PercentExpenseStrategy import PercentExpenseStrategy
from .ExactExpenseStrategy import ExactExpenseStrategy
from ..models.ExpenseType import ExpenseType


class ExpenseStrategyFactory:
    @staticmethod
    def get_expense_strategy(expense_type):
        match expense_type:
            case ExpenseType.EQUAL.name:
                return EqualExpenseStrategy()
            case ExpenseType.EXACT.name:
                return ExactExpenseStrategy()
            case ExpenseType.PERCENT.name:
                return PercentExpenseStrategy()
            case _:
                raise Exception("Invalid expense split type")
