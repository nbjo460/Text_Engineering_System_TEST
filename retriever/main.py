from kafka_tools.producer import Producer
from mongodb_tools.DAL_mongodb import DAL_mongo
import config
from retrieve import Retriever

if __name__ == "__main__":

    DAL_mongo = DAL_mongo(prefix="mongodb+srv",
                          host="cluster0.6ycjkak.mongodb.net/",
                          database="IranMalDB",
                          collection="tweets",
                          user="IRGC_NEW",
                          password="iran135")

    producer = Producer(config.KAFKA_SERVER_URI)

    topics_with_value = {1: config.KAFKA_ANTISEMITIC,0: config.KAFKA_NOT_ANTISEMITIC}
    send_by_field = 'Antisemitic'
    num_documents = 10
    sort_by_field = 'CreateDate'
    retriever = Retriever(DAL_mongo=DAL_mongo,
                          num_documents= num_documents,
                          sort_by_field=sort_by_field)
    documents = retriever.get_next_documents()
