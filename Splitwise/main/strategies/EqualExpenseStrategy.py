from .ExpenseStrategy import ExpenseStrategy
from ..models.User import User
from ..models.Expense import Expense
from ..models.ExpensePayingUser import ExpensePayingUser
from ..models.ExpenseOwingUser import ExpenseOwingUser


class EqualExpenseStrategy(ExpenseStrategy):
    def validate(self, amount_list):
        return True if not amount_list else False

    def add_expense(self, group, total_amount, user_paid_money, description):
        expense = Expense()
        expense.group = group
        expense.amount = total_amount
        expense.created_by = user_paid_money
        expense.description = description
        expense.save()
        return expense

    def add_expense_paying_user(self, expense, user, amount):
        expense_paying_user = ExpensePayingUser()
        expense_paying_user.expense = expense
        expense_paying_user.user = user
        expense_paying_user.amount = amount
        expense_paying_user.save()

    def add_expense_owing_user(self, expense, user, amount):
        expense_owing_user = ExpenseOwingUser()
        expense_owing_user.expense = expense
        expense_owing_user.user = user
        expense_owing_user.amount = amount
        expense_owing_user.save()

    def create_expense(self, group, payment_made_by_user_id, total_amount, no_of_users, users_own_money_list,
                       amount_list=None, description=None):
        if self.validate(amount_list):
            user_paid_money = User.objects.get(id=payment_made_by_user_id)
            expense = self.add_expense(group, total_amount, user_paid_money, description)
            self.add_expense_paying_user(expense, user_paid_money, total_amount)
            money_owning_users = []
            each_user_amount = round(total_amount / no_of_users, 2)
            for user_own_money in users_own_money_list:
                user = User.objects.get(id=user_own_money)
                money_owning_users.append(user)
                self.add_expense_owing_user(expense, user, each_user_amount)
            expense.participants.add(*money_owning_users)
            return expense
        else:
            raise Exception("Amount list should be empty for EqualExpenseStrategy")
