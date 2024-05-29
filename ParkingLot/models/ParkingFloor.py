class ParkingFloor:
    def __init__(self, parking_slots=[], position=None):
        self.parking_slots = parking_slots
        self.position = position

    def display(self):
        print(f"Floor no. {self.position}")
        for slot in self.parking_slots:
            print(slot.display(), end="")
