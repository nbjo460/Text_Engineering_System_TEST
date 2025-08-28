from utils.kafka_tools.consumer import Consumer
from utils.mongodb_tools.DAL_mongodb import DAL_mongo
import config


class Manager:

    def __init__(self):
        self.DAL_mongo_antisemitic = DAL_mongo(config.MONGO_PREFIX,
                                   config.MONGO_HOST,
                                   config.MONGO_DB,
                                   config.MONGO_COLLECTION_ANTISEMITIC)
        self.DAL_mongo_not_antisemitic = DAL_mongo(config.MONGO_PREFIX,
                                   config.MONGO_HOST,
                                   config.MONGO_DB,
                                   config.MONGO_COLLECTION_NOT_ANTISEMITIC)
        self.consumer = Consumer(config.KAFKA_SERVER_URI,
                                config.KAFKA_ANTISEMITIC, config.KAFKA_NOT_ANTISEMITIC)


    def manage_message(self):
        print("processor started")
        self.consumer.run_consumer_events()
        self.DAL_mongo_antisemitic.open_connection()
        self.DAL_mongo_not_antisemitic.open_connection()

        listen_messages = True
        while listen_messages:
            message = self._get_message()
            self.insert_message_to_db(message)
        self.DAL_mongo_antisemitic.close_connection()
        self.DAL_mongo_not_antisemitic.close_connection()


    def _get_message(self):
        print("waiting to message")
        messages = self.consumer.get_events()
        return next(messages)


    def insert_message_to_db(self, message):
        if message.topic == config.KAFKA_ANTISEMITIC:
            self.DAL_mongo_antisemitic.insert_one(message.value)
        elif message.topic == config.KAFKA_NOT_ANTISEMITIC:
            self.DAL_mongo_not_antisemitic.insert_one(message.value)
        else:
            print("ERROR: TOPIC IS NOT RECOGNIZED")

