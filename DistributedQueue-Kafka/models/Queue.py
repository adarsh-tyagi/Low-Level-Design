from .Topic import Topic


class Queue:
    def __init__(self):
        self.topics = {}

    def create_topic(self, name):
        topic = Topic(name)
        self.topics[name] = topic

    def add_subscriber(self, topic_name, subscriber):
        topic = self.topics.get(topic_name, None)
        if topic:
            topic.add_subscriber(subscriber)
        else:
            raise Exception(f"Topic {topic_name} does not exist")

    def remove_subscriber(self, topic_name, subscriber):
        topic = self.topics.get(topic_name, None)
        if topic:
            topic.remove_subscriber(subscriber)
        else:
            raise Exception(f"Topic {topic_name} does not exist")

    def publish_message(self, topic_name, message):
        topic = self.topics.get(topic_name, None)
        if topic:
            topic.add_message(message)
        else:
            raise Exception(f"Topic {topic_name} does not exist")
