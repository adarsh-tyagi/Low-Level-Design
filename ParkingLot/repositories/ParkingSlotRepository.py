from models.ParkingSlot import ParkingSlot
from models.VehicleType import VehicleType
from models.SlotStatus import SlotStatus


class ParkingSlotRepository:
    @staticmethod
    def create_slots(slot_type, slots_count=0):
        parking_slots = []
        if slots_count:
            for slot in range(slots_count):
                parking_slots.append(ParkingSlot(slot_type, SlotStatus.AVAILABLE.name))
        return parking_slots
