import os


MONGO_PREFIX = os.getenv("MONGO_PREFIX", "mongodb+srv")
MONGO_HOST = os.getenv("MONGO_HOST", "cluster0.6ycjkak.mongodb.net/")
MONGO_USER = os.getenv("MONGO_USER", "IRGC_NEW")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD", "iran135")
MONGO_DB = os.getenv("MONGO_DB", "IranMalDB")
MONGO_COLLECTION = os.getenv("MONGO_COLLECTION", "tweets")

KAFKA_SERVER_URI = os.getenv("KAFKA_SERVER_URI", "localhost:9092")
KAFKA_ANTISEMITIC = os.getenv("KAFKA_ANTISEMITIC", "raw_tweets_antisemitic")
KAFKA_NOT_ANTISEMITIC = os.getenv("KAFKA_NOT_ANTISEMITIC", "raw_tweets_not_antisemitic")

