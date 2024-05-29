# Singleton method is a way to provide one and only one object of a particular type. It is useful when you want to
# restrict object creation to only one instance. It is used in logging, driver objects, caching, thread pools, database.

class Singleton:
    __instance = None

    @staticmethod
    def get_instance():
        if Singleton.__instance is None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        if Singleton.__instance is not None:
            raise Exception("This class is of Singleton type")
        else:
            Singleton.__instance = self


if __name__ == "__main__":
    singleton1 = Singleton.get_instance()
    print(singleton1)

    singleton2 = Singleton.get_instance()
    print(singleton2)

    print(singleton1 == singleton2)

    singleton3 = Singleton()
    print(singleton3)
