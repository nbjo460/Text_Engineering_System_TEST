from kafka import KafkaConsumer
import json


class Consumer:

    def __init__(self, server_uri, topic):
        self.server_uri = server_uri
        self.consumer_events = None
        self.topic = topic


    def run_consumer_events(self):
        self.consumer_events = KafkaConsumer(self.topic,
                                 value_deserializer=lambda m: json.loads(m.decode('ascii')),
                                 group_id='text-group',
                                 bootstrap_servers=[self.server_uri])
        print("start to consume events")


    def get_events(self):
        if self.consumer_events is not None:
            for message in self.consumer_events:
                print(f"offset:  {message.offset}")
                print(f"topic:  {message.topic}")

                yield message.value


# if __name__ == '__main__':
#     consumer = Consumer("localhost:9092", "test-topic")
#     consumer.run_consumer_events()
#     events =consumer.get_events()
#     while True:
#         next(events)