from abc import ABC, abstractmethod


class FindParkingSpotStrategy(ABC):
    @abstractmethod
    def find_parking_spot(self, parking_lot, vehicle_type):
        pass
