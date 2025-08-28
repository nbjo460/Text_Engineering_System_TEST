import os

# env variables for mongodb, initialized with current mongodb details
MONGO_PREFIX = os.getenv("MONGO_PREFIX", "mongodb")
MONGO_HOST = os.getenv("MONGO_HOST", "cluster0.6ycjkak.mongodb.net/")
MONGO_USER = os.getenv("MONGO_USER", "IRGC_NEW")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD", "iran135")
MONGO_DB = os.getenv("MONGO_DB", "IranMalDB")
MONGO_COLLECTION_ANTISEMITIC = os.getenv("MONGO_COLLECTION", "tweets_antisemitic")
MONGO_COLLECTION_NOT_ANTISEMITIC = os.getenv("MONGO_COLLECTION", "tweets_not_antisemitic")
