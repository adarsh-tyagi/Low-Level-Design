# Strategy method allows us to define the family of algorithms, encapsulate them and putting each in separate classes
# and make them interchangeable. This method allows the client to choose the algorithm at runtime.


from abc import ABC, abstractmethod


class NavigationStrategy(ABC):
    @abstractmethod
    def navigate(self):
        pass


class CarNavigation(NavigationStrategy):
    def navigate(self):
        print("Navigating using Car")


class BikeNavigation(NavigationStrategy):
    def navigate(self):
        print("Navigating using Bike")


class PedestrianNavigation(NavigationStrategy):
    def navigate(self):
        print("Navigating using Pedestrian")


class Navigator:
    def __init__(self, navigation_strategy):
        self.navigation_strategy = navigation_strategy

    def navigate(self):
        self.navigation_strategy.navigate()


def choose_navigation_strategy():
    user_input = str(input("Enter your strategy (1 for car, 2 for bike and 3 for pedestrian: "))
    if user_input == "1":
        return CarNavigation()
    elif user_input == "2":
        return BikeNavigation()
    elif user_input == "3":
        return PedestrianNavigation()
    else:
        raise ValueError("Invalid input")


if __name__ == "__main__":
    navigation_strategy = choose_navigation_strategy()
    navigator = Navigator(navigation_strategy)
    navigator.navigate()
