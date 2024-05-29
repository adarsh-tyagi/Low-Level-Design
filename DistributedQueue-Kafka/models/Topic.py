class Topic:
    def __init__(self, name):
        self.name = name
        self.subscribers = []
        self.messages = []

    def add_subscriber(self, subscriber):
        self.subscribers.append(subscriber)

    def remove_subscriber(self, subscriber):
        if subscriber in self.subscribers:
            self.subscribers.remove(subscriber)
        else:
            raise Exception(f"Subscriber {subscriber.name} does not exist in topic {self.name}")

    def add_message(self, message):
        self.messages.append(message)
        for subscriber in self.subscribers:
            subscriber.consume_message(message)
