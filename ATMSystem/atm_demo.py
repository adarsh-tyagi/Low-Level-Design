from atm import ATM
from operation_type import OperationType


class ATMDemo:
    @staticmethod
    def main():
        atm = ATM.get_instance()
        
        atm.insert_card("1234-5678-1234-55678")
        atm.enter_pin("1234")
        atm.select_operation(OperationType.CHECK_BALANCE)
        
        atm.insert_card("1234-5678-1234-55678")
        atm.enter_pin("1234")
        atm.select_operation(OperationType.WITHDRAW_CASH, 500)
        
        atm.insert_card("1234-5678-1234-55678")
        atm.enter_pin("1234")
        atm.select_operation(OperationType.DEPOSIT_CASH, 100)
        
        atm.insert_card("1234-5678-1234-55678")
        atm.enter_pin("1234")
        atm.select_operation(OperationType.WITHDRAW_CASH, 2000)
        
        atm.insert_card("1234-5678-1234-55678")
        atm.enter_pin("3412")
        

if __name__ == "__main__":
    ATMDemo.main()