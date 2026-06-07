from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
from Coin import Coin

if TYPE_CHECKING:
    from .Vending_Machine import VendingMachine


class VendingMachineState(ABC):
    def __init__(self, machine: 'VendingMachine'):
        self.machine = machine
        
    @abstractmethod
    def insert_coin(self, coin: Coin):
        pass
    
    @abstractmethod
    def select_item(self, code: str):
        pass
    
    @abstractmethod
    def dispense(self): 
        pass
    
    @abstractmethod
    def refund(self):
        pass
    

class IdleState(VendingMachineState):
    def insert_coin(self, coin):
        print("Please select item before inserting money")
    
    def select_item(self, code):
        if not self.machine.get_inventory().is_available(code):
            print("Item not available")
            return 
        
        self.machine.set_selected_item_code(code)
        from States import ItemSelectState
        self.machine.set_state(ItemSelectedState(self.machine))
        print(f"Item selected: {code}")
    
    def dispense(self):
        print("No Item selected")
    
    def refund(self):
        print("No money to refund")


class ItemSelectedState(VendingMachineState):
    def insert_coin(self, coin):
        self.machine.add_balance(coin.get_value())
        print(f"Coin inserted: {coin.get_value()} $ ({coin.name})")
        
        selected_item = self.machine.get_selected_item()
        if selected_item and self.machine.get_balance() >= selected_item.get_price():
            print("sufficient money recieved")
            from States import HasMoneyState
            self.machine.set_state(HasMoneyState(self.machine))
    
    def select_item(self, code):
        print("Item already selected. Insert money or request refund to select different item")
    
    def dispense(self):
        print("Please insert sufficient money")
    
    def refund(self):
        self.machine.refund_balance()
        self.machine.reset()
        from States import IdleState
        self.machine.set_state(IdleState(self.machine))


class HasMoneyState(VendingMachineState):
    def insert_coin(self, coin: Coin):
        self.machine.add_balance(coin.get_value())
        print(f"Additional coin inserted: {coin.get_value()} $ ({coin.name})")
    
    def select_item(self, code):
        print("Item already selected. Please dispense or request refund to select different item")
    
    def dispense(self):
        from States import DispensingState
        self.machine.set_state(DispensingState(self.machine))
        self.machine.dispense_item()
    
    def refund(self):
        self.machine.refund_balance()
        self.machine.reset()
        from States import IdleState
        self.machine.set_state(IdleState(self.machine))


class DispensingState(VendingMachineState):
    def insert_coin(self, coin):
        print("Dispensing right now. Please wait")
    
    def select_item(self, code):
        print("Currently dispensing. Please wait")
    
    def dispense(self):
        print("In progress...")
    
    def refund(self):
        print("Dispensing in progress. Can not refund dispensed item")