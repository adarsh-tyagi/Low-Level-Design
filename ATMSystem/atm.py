import threading
from atm_state import ATMState, IdleState
from bank_service import BankService
from card import Card
from operation_type import OperationType
from note_dispenser import NoteDispense100, NoteDispense50, NoteDispense20
from cash_dispenser import CashDispenser


class ATM:
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._initialised = False
        return cls._instance
    
    def __init__(self):
        if not self._initialised:
            self._current_state = IdleState()
            self._bank_service = BankService()
            self._current_card = None
            self._transaction_counter = 0
            
            c1 = NoteDispense100(10)
            c2 = NoteDispense50(20)
            c3 = NoteDispense20(30)
            
            c1.set_next_chain(c2)
            c2.set_next_chain(c3)
            self._cash_dispenser = CashDispenser(c1)
            self._initialised = True
            
    @classmethod
    def get_instance(cls):
        return cls()

    def change_state(self, new_state):
        self._current_state = new_state
        
    def set_current_card(self, card):
        self._current_card = card
        
    def insert_card(self, card_number):
        self._current_state.insert_card(self, card_number)
    
    def enter_pin(self, pin):
        self._current_state.enter_pin(self, pin)
    
    def select_operation(self, op, *args):
        self._current_state.select_operation(self, op, *args)
    
    def check_balance(self):
        balance = self._bank_service.get_balance(self._current_card)
        print(f"Your current account balance is: ${balance:.2f}")
    
    def withdraw_cash(self, amount):
        if not self._cash_dispenser.can_dispense_cash(amount):
            raise RuntimeError("Insufficient cash available in the ATM")
        
        self._bank_service.withdraw_money(self._current_card, amount)
        try:
            self._cash_dispenser.dispense_cash(amount)
        except Exception as e:
            self._bank_service.deposit_money(self._current_card, amount)
            raise RuntimeError("something went wrong while dispensing cash, amount not deducted from your account")
    
    def deposit_cash(self, amount):
        self._bank_service.deposit_money(self._current_card, amount)
        print(f"Amount ${amount} is deposited in your account successfully")
    
    def get_current_card(self):
        return self._current_card
    
    def get_bank_service(self):
        return self._bank_service