from strategies.findParkingSpotStrategies.SimpleFindParkingSpotStrategy import SimpleFindParkingSpotStrategy


class FindParkingLotStrategyFactory:
    @staticmethod
    def get_find_parking_spot_strategy(strategy_type=None):
        if strategy_type == "closest":
            return SimpleFindParkingSpotStrategy()
        else:
            return SimpleFindParkingSpotStrategy()
