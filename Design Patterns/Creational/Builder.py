# Builder method aims to separate the construction of a complex object from its representation so that same
# construction process can create different representations. It allows you to create complex objects step by step.
# Using same construction code, we can produce different types and representation of objects easily.


from abc import ABC, abstractmethod


class House:
    def __init__(self, builder):
        self.storey = builder.storey
        self.roof = builder.roof
        self.rooms = builder.rooms


class HouseBuilder:
    def __init__(self):
        self.storey = None
        self.roof = None
        self.rooms = None

    def build_storey(self, storey):
        self.storey = storey
        return self

    def build_roof(self, roof):
        self.roof = roof
        return self

    def build_rooms(self, rooms):
        self.rooms = rooms
        return self

    def build(self):
        return House(self)


class Director:
    def __init__(self, builder):
        self.builder = builder

    def build_villa(self):
        return self.builder.build_storey(2).build_roof("flat").build_rooms(4).build()

    def build_mansion(self):
        return self.builder.build_storey(4).build_roof("slant").build_rooms(10).build()

    def build_apartment(self):
        return self.builder.build_storey(1).build_roof("flat").build_rooms(2).build()


if __name__ == "__main__":
    house_builder = HouseBuilder()
    director = Director(house_builder)
    villa = director.build_villa()
    print(f"Villa: Storey: {villa.storey}, Roof: {villa.roof}, Rooms: {villa.rooms}")
    mansion = director.build_mansion()
    print(f"Mansion: Storey: {mansion.storey}, Roof: {mansion.roof}, Rooms: {mansion.rooms}")
    apartment = director.build_apartment()
    print(f"Apartment: Storey: {apartment.storey}, Roof: {apartment.roof}, Rooms: {apartment.rooms}")

    # create a unique house object using same builder code
    two_bhk_building = house_builder.build_storey(20).build_roof("flat").build_rooms(40).build()
    print(f"2 BHK Building: Storey: {two_bhk_building.storey}, Roof: {two_bhk_building.roof}, Rooms: {two_bhk_building.rooms}")
    