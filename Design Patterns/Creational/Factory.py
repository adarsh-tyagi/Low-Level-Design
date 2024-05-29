# Factory method allows interface or class to create an object but let the subclasses decide which class/object to
# instantiate.
# Objects are created without exposing the logic to the client and for creating new type of object, the client uses
# the same common interface.

class TwoWheeler:
    def __init__(self):
        self.type = "Two Wheeler"

    def get_ride(self):
        print("Getting you two wheeler ride")


class ThreeWheeler:
    def __init__(self):
        self.type = "Three Wheeler"

    def get_ride(self):
        print("Getting you three wheeler ride")


class FourWheeler:
    def __init__(self):
        self.type = "Four Wheeler"

    def get_ride(self):
        print("Getting you four wheeler ride")


def factory(ride_type):
    rides_available = {'TwoWheeler': TwoWheeler, 'ThreeWheeler': ThreeWheeler, 'FourWheeler': FourWheeler}
    return rides_available[ride_type]()


if __name__ == "__main__":
    ride_input = input("Enter the type of ride you want (TwoWheeler, ThreeWheeler or FourWheeler): ")
    ride = factory(ride_input)
    ride.get_ride()
