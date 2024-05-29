class Producer:
    def __init__(self, name):
        self.name = name

    def publish_message(self, topic, message, queue):
        queue.publish_message(topic, message)
        print(f"Producer {self.name} published message {message} to topic {topic}")
