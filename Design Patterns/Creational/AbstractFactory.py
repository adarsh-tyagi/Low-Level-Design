# Abstract Factory Method allows to create the families of related objects without specifying their concrete classes.
# We abstract the creation of objects depending on the logic, business or platform choice, etc.

from abc import ABC, abstractmethod


class Character(ABC):

    @abstractmethod
    def get_character(self):
        pass


class HeroCharacter(Character):

    def get_character(self):
        return "Hero"


class VillainCharacter(Character):

        def get_character(self):
            return "Villain"


class Weapon(ABC):

    @abstractmethod
    def get_weapon(self):
        pass


class Sword(Weapon):

    def get_weapon(self):
        return "Sword"


class Crossbow(Weapon):

    def get_weapon(self):
        return "Crossbow"


class CharacterFactory(ABC):

    @abstractmethod
    def get_character(self):
        pass

    @abstractmethod
    def get_weapon(self):
        pass


class HeroCharacterFactory(CharacterFactory):

    def get_character(self):
        return HeroCharacter()

    def get_weapon(self):
        return Crossbow()


class VillainCharacterFactory(CharacterFactory):

    def get_character(self):
        return VillainCharacter()

    def get_weapon(self):
        return Sword()


def create_game_objects(factory):
    character = factory.get_character()
    weapon = factory.get_weapon()
    print(f"Character: {character.get_character()} uses Weapon: {weapon.get_weapon()}")


if __name__ == "__main__":
    hero_factory = HeroCharacterFactory()
    villain_factory = VillainCharacterFactory()

    create_game_objects(hero_factory)
    create_game_objects(villain_factory)
