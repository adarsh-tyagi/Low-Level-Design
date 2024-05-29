import datetime


class Ticket:
    def __init__(self, parking_lot_name, floor_number, slot_number, vehicle):
        self.parking_lot_name = parking_lot_name
        self.floor_number = floor_number
        self.slot_number = slot_number
        self.vehicle = vehicle
        self.entry_time = datetime.datetime.now()

    def get_ticket_id(self):
        return f"{self.parking_lot_name}_{self.floor_number}_{self.slot_number}"
