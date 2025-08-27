from kafka_tools.consumer import Consumer
from kafka_tools.producer import Producer
from mongodb_tools.DAL_mongodb import DAL_mongo


class Manager:
    def __init__(self):
        dal = DAL_mongo()
        consumer = Consumer()
        producer = Producer()
