import time
from utils.kafka_tools.producer import Producer
from utils.mongodb_tools.DAL_mongodb import DAL_mongo
import config
from retrieve import Retriever
from publish import Publish



if __name__ == "__main__":

    DAL_mongo = DAL_mongo(prefix= config.MONGO_PREFIX,
                          host= config.MONGO_HOST,
                          database= config.MONGO_DB,
                          collection= config.MONGO_COLLECTION,
                          user= config.MONGO_USER,
                          password= config.MONGO_PASSWORD)

    producer = Producer(config.KAFKA_SERVER_URI)
    retriever = Retriever(DAL_mongo, config.NUM_DOCUMENTS, config.SORT_BY_FIELD)
    publish = Publish(producer, config.MATCH_TOPICS, config.CLASSIFIED)



    while True:
        documents = retriever.get_next_documents()
        publish.publish_messages(documents)
        time.sleep(config.TIME_SLEEP)


