# Observer method allows you to create the subscription mechanism to send the notification to the multiple objects
# about any new event happens to the object that they are observing.


from abc import ABC, abstractmethod


class Observable:
    def __init__(self):
        self.observers = []

    def register(self, observer):
        self.observers.append(observer)

    def unregister(self, observer):
        self.observers.remove(observer)

    def notify_observers(self, message):
        for observer in self.observers:
            observer.notify(message)


class Bitcoin:

    def __init__(self, price):
        self.price = price

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price


class BitcoinTracker(Observable):

    def __init__(self, bitcoin):
        super().__init__()
        self.bitcoin = bitcoin

    def set_bitcoin_price(self, price):
        if price != self.bitcoin.get_price():
            notification_message = f"Bitcoin price changed from {self.bitcoin.get_price()} to {price}"
            self.bitcoin.set_price(price)
            self.notify_observers(notification_message)


class Observer(ABC):
    @abstractmethod
    def notify(self, message):
        pass


class EmailSender(Observer):
    def notify(self, message):
        print("*** Email Notification ***")
        print(message)


class SMSSender(Observer):
    def notify(self, message):
        print("*** SMS Notification ***")
        print(message)


if __name__ == "__main__":
    bitcoin = Bitcoin(100000)
    bitcoin_tracker = BitcoinTracker(bitcoin)
    bitcoin_tracker.register(EmailSender())
    bitcoin_tracker.register(SMSSender())

    bitcoin_tracker.set_bitcoin_price(200000)
    bitcoin_tracker.set_bitcoin_price(30000)
