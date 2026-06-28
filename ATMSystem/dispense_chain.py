from abc import ABC, abstractmethod

class DispenseChain(ABC):
    @abstractmethod
    def set_next_chain(self, next_chain):
        pass
    
    @abstractmethod
    def dispense(self, amount):
        pass
    
    @abstractmethod
    def can_dispense(self, amount):
        pass