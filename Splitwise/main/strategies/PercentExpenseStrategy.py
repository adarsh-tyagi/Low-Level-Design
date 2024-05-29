from .ExpenseStrategy import ExpenseStrategy
from ..models.User import User
from ..models.Expense import Expense
from ..models.ExpensePayingUser import ExpensePayingUser
from ..models.ExpenseOwingUser import ExpenseOwingUser


class PercentExpenseStrategy(ExpenseStrategy):
    def validate(self, no_of_users, amount_list):
        return amount_list and (len(amount_list) == no_of_users) and sum(amount_list) == 100

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
        if self.validate(no_of_users, amount_list):
            user_paid_money = User.objects.get(id=payment_made_by_user_id)
            expense = self.add_expense(group, total_amount, user_paid_money, description)
            self.add_expense_paying_user(expense, user_paid_money, total_amount)
            money_owning_users = []
            for i, user_own_money in enumerate(users_own_money_list):
                user = User.objects.get(id=user_own_money)
                money_owning_users.append(user)
                self.add_expense_owing_user(expense, user, round(total_amount * amount_list[i] / 100, 2))
            expense.participants.add(*money_owning_users)
            return expense
        else:
            raise Exception("Percent amount list does not match no. of users or total value to 100%")
