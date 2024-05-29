# Prototype method aims to create a new object by copying an existing object, known as prototype. It allows you to copy
# the existing object independent of their concrete class implementation.


from abc import ABC, abstractmethod


class Enemy(ABC):
    @abstractmethod
    def clone(self):
        pass

    @abstractmethod
    def power(self):
        pass


class Electro(Enemy):
    def clone(self):
        return Electro()

    def power(self):
        return "Electric Shock"


class Sandman(Enemy):
    def clone(self):
        return Sandman()

    def power(self):
        return "Sand Attack"


class EnemyRegistry:
    def __init__(self):
        self.prototypes = {}

    def add_enemy(self, enemy_type, enemy):
        self.prototypes[enemy_type] = enemy

    def get_enemy(self, enemy_type):
        return self.prototypes[enemy_type].clone()


if __name__ == "__main__":
    electro = Electro()
    sandman = Sandman()

    enemy_registry = EnemyRegistry()
    enemy_registry.add_enemy("Electro", electro)
    enemy_registry.add_enemy("Sandman", sandman)

    cloned_electro = enemy_registry.get_enemy("Electro")
    print(f"Cloned Electro: {cloned_electro.power()}")

    cloned_sandman = enemy_registry.get_enemy("Sandman")
    print(f"Cloned Sandman: {cloned_sandman.power()}")

