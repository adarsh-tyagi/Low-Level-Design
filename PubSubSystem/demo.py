from pub_sub_service import PubSubService
from subscriber import NewsSubscriber, AlertSubscriber
from message import Message
import time

class Demo:
    @staticmethod
    def main():
        pubsubservice = PubSubService.get_instance()
        
        # create subscribers
        sub1 = NewsSubscriber("ABC")
        sub2 = AlertSubscriber("XYZ")
        
        # create topic and subscriptions
        SPORTS_TOPIC = "SPORTS"
        pubsubservice.create_topic(SPORTS_TOPIC)
        
        pubsubservice.subscribe(SPORTS_TOPIC, sub1)
        pubsubservice.subscribe(SPORTS_TOPIC, sub2)
        
        # publish to sports topic
        pubsubservice.publish(SPORTS_TOPIC, Message("India won the world test championship"))
        
        # unsubscribe from topic
        pubsubservice.unsubscribe(SPORTS_TOPIC, sub2)
        
        pubsubservice.shutdown()

        

if __name__ == "__main__":
    Demo.main()