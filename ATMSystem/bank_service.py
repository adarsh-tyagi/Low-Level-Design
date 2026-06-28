from account import Account
from card import Card


class BankService:
    def __init__(self):
        self.accounts = {}
        self._cards = {}
        self._card_account_map = {}
        
        account1 = self.create_account("1234567890", 1000.0)
        card1 = self.create_card("1234-5678-1234-5678", "1234")
        self.link_card_to_account(card1, account1)
        
        account2 = self.create_account("9876543201", 500.0)
        card2 = self.create_card("9876-5678-5432-4321", "7890")
        self.link_card_to_account(card2, account2)
        
    def create_account(self, account_number, initial_balance):
        account = Account(account_number, initial_balance)
        self.accounts[account_number] = account
        return account
    
    def create_card(self, card_number, pin):
        card = Card(card_number, pin)
        self._cards[card_number] = card
        return card
    
    def authenticate(self, card, pin):
        return card.get_pin() == pin
    
    def authenticate_card(self, card_number):
        return self._cards.get(card_number)
    
    def get_balance(self, card):
        return self._card_account_map[card].get_balance()

    def withdraw_money(self, card, amount):
        self._card_account_map[card].withdraw(amount)
    
    def deposit_money(self, card, amount):
        self._card_account_map[card].deposit(amount)
    
    def link_card_to_account(self, card, account):
        account.get_cards()[card.get_card_number()] = card
        self._card_account_map[card] = account