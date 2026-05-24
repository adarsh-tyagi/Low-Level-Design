class Compartment:
    def __init__(self, size):
        self.size = size
        self.occupied = False
    
    def get_size(self):
        return self.size

    def is_occupied(self) -> bool:
        return self.occupied

    def mark_occupied(self) -> None:
        self.occupied = True
    
    def mark_free(self) -> None:
        self.occupied = False
    
    def open(self) -> None:
        pass