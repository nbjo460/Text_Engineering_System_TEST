from utils.kafka_tools.consumer import Consumer
from utils.kafka_tools.producer import Producer
import config
from utils.cleaner import Cleaner


class Manager:
    def __init__(self):
        self.consumer = Consumer(config.KAFKA_SERVER_URI,
                                 config.SOURCE_ANTISEMITIC_TWEETS_TOPIC,
                                 config.SOURCE_NOT_ANTISEMITIC_TWEETS_TOPIC)
        self.producer = Producer(config.KAFKA_SERVER_URI)

    def manage_message(self):
        print("processor started")
        self.consumer.run_consumer_events()
        listen_messages = True
        while listen_messages:
            message = self._get_message()
            processed_message = self._process_message(message)
            self._send_message(processed_message)

    def _get_message(self):
        print("waiting to message")
        messages = self.consumer.get_events()
        return next(messages)

    def _process_message(self, _message):
        print("cleaning message")
        uncleaned_text = _message.value[config.ORIGINAL_TEXT_FIELD]
        cleaner = Cleaner(uncleaned_text)
        cleaned_text = cleaner.clean()
        _message.value["clean_text"] = cleaned_text
        return _message

    def _send_message(self, _processed_message):
        print("sending message")
        self.producer.create_producer()

        if _processed_message.topic == config.SOURCE_ANTISEMITIC_TWEETS_TOPIC:
            topic = config.DESTINATION_ANTISEMITIC_TWEETS_TOPIC
            self.producer.publish_messages(topic, _processed_message.value)

        elif _processed_message.topic == config.SOURCE_NOT_ANTISEMITIC_TWEETS_TOPIC:
            topic = config.DESTINATION_NOT_ANTISEMITIC_TWEETS_TOPIC
            self.producer.publish_messages(topic, _processed_message.value)

        else:
            print("ERROR: SOURCE TOPIC IS NOT RECOGNIZED")

