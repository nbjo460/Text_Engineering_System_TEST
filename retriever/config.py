import os

# env variables for mongodb, initialized with current mongodb details
MONGO_PREFIX = os.getenv("MONGO_PREFIX", "mongodb+srv")
MONGO_HOST = os.getenv("MONGO_HOST", "cluster0.6ycjkak.mongodb.net/")
MONGO_USER = os.getenv("MONGO_USER", "IRGC_NEW")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD", "iran135")
MONGO_DB = os.getenv("MONGO_DB", "IranMalDB")
MONGO_COLLECTION = os.getenv("MONGO_COLLECTION", "tweets")

# env uri for kafka, initialized with localhost uri
KAFKA_SERVER_URI = os.getenv("KAFKA_SERVER_URI", "localhost:9092")

# global variables with two names of topics
KAFKA_ANTISEMITIC = "raw_tweets_antisemitic"
KAFKA_NOT_ANTISEMITIC = "raw_tweets_not_antisemitic"

# global variables for app - retriever
MATCH_TOPICS = {1: KAFKA_ANTISEMITIC, 0: KAFKA_NOT_ANTISEMITIC} # topics vs match values in data
NUM_DOCUMENTS = 5
CLASSIFIED = 'Antisemitic'
SORT_BY_FIELD = 'CreateDate'
TIME_SLEEP = 10

