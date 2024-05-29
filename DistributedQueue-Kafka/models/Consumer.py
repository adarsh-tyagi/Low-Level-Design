class Consumer:
    def __init__(self, name):
        self.name = name

    def consume_message(self, message):
        print(f"Consumer {self.name} received message {message}")
