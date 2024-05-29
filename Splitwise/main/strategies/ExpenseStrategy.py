from abc import ABC, abstractmethod


class ExpenseStrategy(ABC):
    @abstractmethod
    def create_expense(self, group, payment_made_by_user_id, total_amount, no_of_users, users_own_money_list,
                       amount_list=None, description=None):
        pass
