from strategies.findParkingSpotStrategies.FindParkingSpotStrategy import FindParkingSpotStrategy
from models.SlotStatus import SlotStatus


class SimpleFindParkingSpotStrategy(FindParkingSpotStrategy):
    def find_parking_spot(self, parking_lot, vehicle_type):
        for floor in parking_lot.parking_floors:
            for spot in floor.parking_slots:
                if spot.slot_type == vehicle_type and spot.slot_status == SlotStatus.AVAILABLE.name:
                    return floor, spot
        return None, None
