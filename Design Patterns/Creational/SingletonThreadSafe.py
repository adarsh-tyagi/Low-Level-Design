from threading import Lock, Thread
from random import shuffle


class SingletonMeta(type):
    _instances = {}
    _lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def __init__(self, value):
        self.value = value


def test_singleton(value):
    singleton = Singleton(value)
    print(singleton.value)


def run_shuffle_thread(threads):
    shuffle(threads)
    for thread in threads:
        thread.start()
        thread.join()


if __name__ == "__main__":
    thread_1 = Thread(target=test_singleton, args=(10,))
    thread_2 = Thread(target=test_singleton, args=(20,))
    thread_3 = Thread(target=test_singleton, args=(30,))
    thread_4 = Thread(target=test_singleton, args=(40,))
    thread_5 = Thread(target=test_singleton, args=(50,))

    run_shuffle_thread([thread_1, thread_2, thread_3, thread_4, thread_5])
