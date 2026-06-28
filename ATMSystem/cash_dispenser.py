import threading
from dispense_chain import DispenseChain


class CashDispenser:
    def __init__(self, chain):
        self._chain = chain
        self._lock = threading.Lock()
        
    def dispense_cash(self, amount):
        with self._lock:
            self._chain.dispense(amount)
    
    def can_dispense_cash(self, amount):
        with self._lock:
            if amount % 10 != 0:
                return False
            return self._chain.can_dispense(amount)