from models.Queue import Queue
from models.Producer import Producer
from models.Consumer import Consumer


class QueueController:
    def __init__(self):
        self.queue = Queue()
        self.producers = {}
        self.consumers = {}

    def get_queue(self):
        return self.queue

    def create_topic(self, name):
        self.queue.create_topic(name)

    def add_producer(self, name):
        self.producers[name] = Producer(name)

    def add_consumer(self, name):
        self.consumers[name] = Consumer(name)

    def add_subscriber(self, topic_name, subscriber_name):
        subscriber = self.consumers.get(subscriber_name)
        self.queue.add_subscriber(topic_name, subscriber)

    def remove_subscriber(self, topic_name, subscriber_name):
        subscriber = self.consumers.get(subscriber_name)
        self.queue.remove_subscriber(topic_name, subscriber)

    def get_producer(self, producer_name):
        return self.producers.get(producer_name)

    def get_topics(self):
        return self.queue.topics.keys()

    def get_subscribers(self, topic_name):
        topic = self.queue.topics.get(topic_name, None)
        if topic:
            return [subscriber.name for subscriber in topic.subscribers]
        else:
            raise Exception(f"Topic {topic_name} does not exist")
