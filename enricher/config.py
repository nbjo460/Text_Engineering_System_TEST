import os
SOURCE_ANTISEMITIC_TWEETS_TOPIC = "preprocessed_tweets_antisemitic"
SOURCE_NOT_ANTISEMITIC_TWEETS_TOPIC = "preprocessed_tweets_not_antisemitic"

DESTINATION_ANTISEMITIC_TWEETS_TOPIC = "enriched_preprocessed_tweets_not_antisemitic"
DESTINATION_NOT_ANTISEMITIC_TWEETS_TOPIC = "enriched_preprocessed_tweets_not_antisemitic"


# env uri for kafka, initialized with localhost uri
KAFKA_SERVER_URI = os.getenv("KAFKA_SERVER_URI", "localhost:9092")

ORIGINAL_TEXT_FIELD = 'text'