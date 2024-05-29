from ..models.Group import Group
from ..models.Expense import Expense
from ..strategies.ExpenseStrategyFactory import ExpenseStrategyFactory


class ExpenseService:
    @staticmethod
    def get_expenses(group_id):
        group = Group.objects.get(id=group_id)
        if group is None:
            raise Exception("Group not found")

        expenses = Expense.objects.filter(group=group)
        return expenses

    @staticmethod
    def add_expense(group_id, payment_made_by_user_id, total_amount, no_of_users, users_own_money_list, expense_type,
                    expense_description, amount_list):
        group = Group.objects.get(id=group_id)
        if group is None:
            raise Exception("Group not found")
        expense_strategy = ExpenseStrategyFactory.get_expense_strategy(expense_type)
        expense = expense_strategy.create_expense(group, payment_made_by_user_id, total_amount, no_of_users,
                                                  users_own_money_list, amount_list, expense_description)
        return expense
