from abc import ABC, abstractmethod
from operation_type import OperationType


class ATMState(ABC):
    @abstractmethod
    def insert_card(self, atm, card_number):
        pass
    
    @abstractmethod
    def enter_pin(self, atm, pin):
        pass
    
    @abstractmethod
    def select_operation(self, atm, op, *args):
        pass
    
    @abstractmethod
    def eject_card(self, atm):
        pass
    
    
class IdleState(ATMState):
    def insert_card(self, atm, card_number):
        print("Card has been inserted")
        card = atm.get_bank_service().authenticate_card(card_number)
        
        if card is None:
            self.eject_card(atm)
        else:
            atm.set_current_card(card)
            atm.change_state(HasCardState())
        
    def enter_pin(self, atm, pin):
        print("Please insert card first")
    
    def select_operation(self, atm, op,  *args):
        print("Please insert card first")
    
    def eject_card(self, atm):
        print("Card not found")
        
class HasCardState(ATMState):
    def insert_state(self, atm, card_number):
        print("card is already inserted")
    
    def enter_pin(self, atm, pin):
        print("Authenticating pin...")
        card = atm.get_current_card()
        is_authenticated = atm.get_bank_service().authenticate(card, pin)
        
        if is_authenticated:
            print("Authentication successful")
            atm.change_state(AuthenticatedState())
        else:
            print("Authentication failed: incorrect pin")
            self.eject_card(atm)
    
    def select_operation(self, atm, op,  *args):
        print("Enter your pin first to use the card")
    
    def eject_card(self, atm):
        print("Card has been ejected")
        atm.set_current_card(None)
        atm.change_state(IdleState())

class AuthenticatedState(ATMState):
    def insert_card(self, atm, card_number):
        print("Card is already inserted and authenticated")
    
    def enter_pin(self, atm, pin):
        print("Card PIN is alreday verified")
    
    def select_operation(self, atm, op,  *args):
        if op == OperationType.CHECK_BALANCE:
            atm.check_balance()
        elif op == OperationType.WITHDRAW_CASH:
            if len(args) == 0 or args[0] <= 0:
                print("Invalid withdrawal amount")
                return
            
            amount_to_withdraw = args[0]
            account_balance = atm.get_bank_service().get_balance(atm.get_current_card())
            
            if amount_to_withdraw > account_balance:
                print("Insufficient balance")
                return 

            print(f"Processing withdrawal for: ${amount_to_withdraw}")
            atm.withdraw_cash(amount_to_withdraw)
        elif op == OperationType.DEPOSIT_CASH:
            if len(args) == 0 or args[0] <= 0:
                print("Invalid deposit amount specified")
                return 
            
            amount_to_deposit = args[0]
            print(f"processing deposit for ${amount_to_deposit}")
            atm.deposit_cash(amount_to_deposit)
        else:
            print("Invalid operation type")
            return 
        
        print("Transaction complete")
        self.eject_card(atm)
        
    def eject_card(self, atm):
        print("Card has been ejected")
        atm.set_current_card(None)
        atm.change_state(IdleState())