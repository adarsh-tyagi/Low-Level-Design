from ..models.Group import Group
from ..models.Expense import Expense
from ..models.ExpensePayingUser import ExpensePayingUser
from ..models.ExpenseOwingUser import ExpenseOwingUser
from ..models.Transaction import Transaction
from collections import defaultdict
import heapq as hq


class Record:
    def __init__(self, user, amount):
        self.user = user
        self.amount = amount

    def __gt__(self, other):
        return self.amount > other.amount


class GroupBalanceSettleUpService:
    def get_group_balance_for_user(self, group_id, user_id=None):
        group_balance = self.get_all_group_balance(group_id)
        user_balance = []
        for k, v in group_balance.items():
            key = k.split(",")
            if user_id:
                if user_id in key:
                    if v > 0:
                        user_balance.append(f"{key[1]} owes {key[0]} : {abs(v)}")
                    elif v < 0:
                        user_balance.append(f"{key[0]} owes {key[1]} : {abs(v)}")
            else:
                if v > 0:
                    user_balance.append(f"{key[1]} owes {key[0]} : {abs(v)}")
                elif v < 0:
                    user_balance.append(f"{key[0]} owes {key[1]} : {abs(v)}")
        return user_balance

    def get_all_group_balance(self, group_id):
        group = Group.objects.get(id=group_id)
        if not group:
            raise Exception("Group not found")
        expenses = Expense.objects.filter(group=group)
        group_participants = group.participants.all()
        group_balance = {}
        for participant_i in range(len(group_participants)-1):
            for participant_j in range(participant_i+1, len(group_participants)):
                group_balance[f"{group_participants[participant_i].id},{group_participants[participant_j].id}"] = 0

        for expense in expenses:
            expense_paying_user = ExpensePayingUser.objects.get(expense=expense)
            expense_owing_users = ExpenseOwingUser.objects.filter(expense=expense)
            for expense_owing_user in expense_owing_users:
                balance_key1 = f"{expense_paying_user.user.id},{expense_owing_user.user.id}"
                balance_key2 = f"{expense_owing_user.user.id},{expense_paying_user.user.id}"
                if balance_key1 in group_balance:
                    group_balance[balance_key1] += expense_owing_user.amount
                elif balance_key2 in group_balance:
                    group_balance[balance_key2] -= expense_owing_user.amount
        return group_balance

    def settle_up_group_balance(self, group_id):
        group = Group.objects.get(id=group_id)
        if not group:
            raise Exception("Group not found")
        expenses = Expense.objects.filter(group=group)
        expense_paying_users = []
        expense_owing_users = []
        for expense in expenses:
            paying_user = ExpensePayingUser.objects.filter(expense=expense)
            owing_users = ExpenseOwingUser.objects.filter(expense=expense)
            expense_paying_users.extend(paying_user)
            expense_owing_users.extend(owing_users)

        money_balance = defaultdict()
        for paying_user in expense_paying_users:
            user = paying_user.user
            amount = paying_user.amount
            money_balance[user] = money_balance.get(user, 0) + amount

        for owing_user in expense_owing_users:
            user = owing_user.user
            amount = owing_user.amount
            money_balance[user] = money_balance.get(user, 0) - amount

        pay_user_money_heap = []
        owe_user_money_heap = []
        for user, amount in money_balance.items():
            record = Record(user, amount)
            if amount > 0:
                hq.heappush(pay_user_money_heap, (-amount, record))
            elif amount < 0:
                hq.heappush(owe_user_money_heap, (amount, record))

        transactions = []
        while len(owe_user_money_heap):
            pay_record = hq.heappop(pay_user_money_heap)
            owe_record = hq.heappop(owe_user_money_heap)
            if abs(pay_record[0]) >= abs(owe_record[0]):
                transactions.append(Transaction(sender=owe_record[1].user, receiver=pay_record[1].user,
                                                amount=abs(owe_record[0])))
                new_pay_amount = abs(pay_record[0]) - abs(owe_record[0])
                record = Record(pay_record[1].user, new_pay_amount)
                hq.heappush(pay_user_money_heap, (-new_pay_amount, record))
            else:
                transactions.append(Transaction(sender=owe_record[1].user, receiver=pay_record[1].user,
                                                amount=abs(pay_record[0])))
                new_owe_amount = abs(owe_record[0]) - abs(pay_record[0])
                record = Record(owe_record[1].user, new_owe_amount)
                hq.heappush(owe_user_money_heap, (-new_owe_amount, record))
        transactions = self.simplify_transactions(transactions)
        return transactions

    def simplify_transactions(self, transactions):
        simplified_transactions = []
        for transaction in transactions:
            sender = transaction.sender.id
            receiver = transaction.receiver.id
            amount = transaction.amount
            transaction_statement = f"{sender} needs to give money to {receiver}: {amount}"
            simplified_transactions.append(transaction_statement)
        return simplified_transactions
