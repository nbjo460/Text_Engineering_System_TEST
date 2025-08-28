import os

# env variables for mongodb, initialized with local mongodb details
MONGO_PREFIX = os.getenv("MONGO_PREFIX", "mongodb")
MONGO_HOST = os.getenv("MONGO_HOST", "localhost")
MONGO_USER = os.getenv("MONGO_USER", "")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD", "")
MONGO_DB = os.getenv("MONGO_DB", "IranMalDB")

MONGO_COLLECTION_ANTISEMITIC = os.getenv("MONGO_COLLECTION_ANTISEMITIC", "tweets_antisemitic")
MONGO_COLLECTION_NOT_ANTISEMITIC = os.getenv("MONGO_COLLECTION_NOT_ANTISEMITIC", "tweets_not_antisemitic")

# env uri for kafka, initialized with localhost uri
KAFKA_SERVER_URI = os.getenv("KAFKA_SERVER_URI", "localhost:9092")

# global variables with two names of topics
KAFKA_ANTISEMITIC = "enriched_preprocessed_tweets_antisemitic"
KAFKA_NOT_ANTISEMITIC = "enriched_preprocessed_tweets_not_antisemitic"

# global variables for app - retriever
MATCH_COLLECTIONS = {KAFKA_ANTISEMITIC: MONGO_COLLECTION_ANTISEMITIC,
                     KAFKA_NOT_ANTISEMITIC: MONGO_COLLECTION_NOT_ANTISEMITIC}

