from controllers.QueueController import QueueController
from threading import Thread


def main():
    print("Welcome to Distributed Queue")

    queue_controller = QueueController()
    queue = queue_controller.get_queue()
    queue_controller.add_producer("producer1")
    queue_controller.add_producer("producer2")
    queue_controller.add_consumer('consumer1')
    queue_controller.add_consumer('consumer2')
    queue_controller.add_consumer('consumer3')
    queue_controller.add_consumer('consumer4')
    queue_controller.add_consumer('consumer5')

    while True:
        command = input("Enter command: ")
        commands = command.split(" ")
        match commands[0].lower():
            case 'exit':
                break
            case 'create_topic':
                queue_controller.create_topic(commands[1])
            case 'show_topics':
                print(queue_controller.get_topics())
            case 'add_subscriber':
                queue_controller.add_subscriber(commands[1], commands[2])
            case 'remove_subscriber':
                queue_controller.remove_subscriber(commands[1], commands[2])
            case 'publish_message':
                producer_name = input("Enter producer name: ")
                producer = queue_controller.get_producer(producer_name)
                topic = input("Enter topic name: ")
                messages = input("Enter multiple messages (comma separated): ")
                messages = messages.split(",")
                threads = []
                for message in messages:
                    thread = Thread(target=producer.publish_message, args=(topic, message, queue))
                    threads.append(thread)
                for thread in threads:
                    thread.start()
                for thread in threads:
                    thread.join()
    print("Exiting from Queue, Bye!")


if __name__ == '__main__':
    main()
