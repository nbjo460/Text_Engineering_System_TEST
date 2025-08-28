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

    def