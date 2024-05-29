class ParkingLot:
    def __init__(self, parking_lot_name, parking_floors=[]):
        self.parking_lot_name = parking_lot_name
        self.parking_floors = parking_floors

    def display(self):
        print(f"Parking lot: {self.parking_lot_name}")
        print("-"*30)
        for floor in self.parking_floors:
            floor.display()
            print("\n")
