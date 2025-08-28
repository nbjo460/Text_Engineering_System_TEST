import os

# env variables for mongodb, initialized with current mongodb details
MONGO_PREFIX = os.getenv("MONGO_PREFIX", "mongodb")
MONGO_HOST = os.getenv("MONGO_HOST", "localhost:27017")
MONGO_USER = os.getenv("MONGO_USER", "")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD", "")
MONGO_DB = os.getenv("MONGO_DB", "IranMalDB")
MONGO_COLLECTION_ANTISEMITIC = os.getenv("MONGO_COLLECTION", "tweets_antisemitic")
MONGO_COLLECTION_NOT_ANTISEMITIC = os.getenv("MONGO_COLLECTION", "tweets_not_antisemitic")
