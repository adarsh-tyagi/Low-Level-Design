# Flyweight method focuses on minimizing the number of objects that are required by the program at the run time.
# Basically it creates a flyweight object that is shared by multiple contexts.
# We create a flyweight class which stored the intrinsic state (which will be shared) and different object with
# extrinsic state (which will be different for each object).


# Flyweight class
class Bullet:
    def __init__(self, image):
        self.image = image


# extrinsic state classes
class FlyingBullet:
    def __init__(self, x, y, z, radius, direction, speed, status, bullet_type, bullet):
        self.x = x
        self.y = y
        self.z = z
        self.radius = radius
        self.direction = direction
        self.speed = speed
        self.status = status
        self.bullet_type = bullet_type
        self.bullet = bullet


# flyweight registry to create and manage flyweight classes
class BulletRegistry:
    def __init__(self):
        self.bullets = {}

    def get_bullet(self, bullet_type):
        return self.bullets.get(bullet_type)

    def add_bullet(self, bullet_type, bullet):
        self.bullets[bullet_type] = bullet

