from Vending_Machine import VendingMachine
from Coin import Coin


class VendingMachineDemo:
    @staticmethod
    def main():
        vending_machine = VendingMachine.get_instance()
        
        vending_machine.add_item("A", "Coke", 25, 3)
        vending_machine.add_item("B", "Lays", 20, 10)
        vending_machine.add_item("C", "Max Protein Bar", 50, 5)
        
        print("Select an item ---")
        vending_machine.select_item("B")
        
        print("Insert the coin ---")
        vending_machine.insert_coin(Coin.TEN)
        vending_machine.insert_coin(Coin.TEN)
        
        print("Dispense item ---")
        vending_machine.dispense()
        
    
if __name__ == "__main__":
    VendingMachineDemo.main()