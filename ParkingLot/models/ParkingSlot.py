from models.SlotStatus import SlotStatus
from models.VehicleType import VehicleType


class ParkingSlot:
    def __init__(self, slot_type, slot_status, vehicle=None, position=None):
        self.slot_type = slot_type
        self.slot_status = slot_status
        self.vehicle = vehicle
        self.position = position

    def display(self):
        if self.slot_status == SlotStatus.AVAILABLE.name:
            slot_status = "A"
        elif self.slot_status == SlotStatus.PARKED.name:
            slot_status = "P"
        elif self.slot_status == SlotStatus.UNAVAILABLE.name:
            slot_status = "U"
        else:
            slot_status = ""

        if self.slot_type == VehicleType.BIKE.name:
            slot_type = "BIKE"
        elif self.slot_type == VehicleType.CAR.name:
            slot_type = "CAR"
        elif self.slot_type == VehicleType.TRUCK.name:
            slot_type = "TRUCK"
        else:
            slot_type = ""
        return f" [status|type: {slot_status} | {slot_type}] "
