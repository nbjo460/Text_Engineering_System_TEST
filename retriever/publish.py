from kafka_tools.producer import Producer


class Publish:

    def __init__(self, producer: Producer, match_topics: dict, classified: str):
        self.producer = producer
        self.match_topics = match_topics
        self.classified = classified


    def publish_messages(self, documents: dict):
        self.producer.create_producer()
        for document in documents:
            try:
                print(document)
                current_value = document[self.classified]
                #print(current_value)
                current_topic = self.match_topics[current_value]
                print(current_topic)
                self.producer.publish_messages(current_topic, document)
            except Exception as e:
                print(f"Error to send document to kafka: {e}")

        self.producer.close_producer()




