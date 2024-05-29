# Bridge method allows us to separate the implementation specific abstraction and implementation independent abstraction
# from each other and can be developed considering as single entities.

# these two api are implementation specific
class CuboidProducingApiOne:

    def produce(self, length, width, height):
        print(f"Cuboid of length {length}, width {width} and height {height} is produced")


class CuboidProducingApiTwo:

    def produce(self, length, width, height):
        print(f"Cuboid of length {length}, width {width} and height {height} is produced")


class Cuboid:

    def __init__(self, length, width, height, api):
        self.length = length
        self.width = width
        self.height = height
        self.api = api

    def produce(self):
        self.api.produce(self.length, self.width, self.height)

    # this method is implementation independent
    def expand(self, factor):
        self.length *= factor
        self.width *= factor
        self.height *= factor
        self.produce()


if __name__ == "__main__":
    cuboid_one = Cuboid(10, 20, 30, CuboidProducingApiOne())
    cuboid_one.produce()
    cuboid_one.expand(2)

    cuboid_two = Cuboid(10, 20, 30, CuboidProducingApiTwo())
    cuboid_two.produce()
    cuboid_two.expand(4)

