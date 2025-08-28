@REM create network to all services:
docker network create text_net

@REM create container of mongodb:
docker run -d --name mongodb --network text_net -p 27017:17017 mongo:latest

@REM  create container of kafka with routing to his name - designed to work inside Docker:
docker run -d --name broker --network text_net -e KAFKA_NODE_ID=1 -e KAFKA_PROCESS_ROLES=broker,controller -e KAFKA_LISTENERS=PLAINTEXT://:9092,CONTROLLER://:9093 -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://broker:9092   -e KAFKA_CONTROLLER_LISTENER_NAMES=CONTROLLER   -e KAFKA_LISTENER_SECURITY_PROTOCOL_MAP=CONTROLLER:PLAINTEXT,PLAINTEXT:PLAINTEXT   -e KAFKA_CONTROLLER_QUORUM_VOTERS=1@broker:9093   -e KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR=1  -e KAFKA_TRANSACTION_STATE_LOG_REPLICATION_FACTOR=1  -e KAFKA_TRANSACTION_STATE_LOG_MIN_ISR=1   -e KAFKA_GROUP_INITIAL_REBALANCE_DELAY_MS=0  -e KAFKA_NUM_PARTITIONS=3  apache/kafka:latest

@REM alternatively, for local work - create container of kafka with routing to localhost:
docker run -d --name broker -p 9092:9092  apache/kafka:latest

@REM  create images and containers to five services - run all the commands below from root-folder-project /Text_Engineering_System_TEST:
docker build -f .\retriever\Dockerfile   -t retriever .
docker run -d --name retriever retriever

docker build -f .\preprocessor\Dockerfile   -t preprocessor .
docker run -d --name preprocessor -e KAFKA_SERVER_URI=broker --network text_net  preprocessor

docker build -f .\enricher\Dockerfile   -t enricher .
docker run -d --name enricher -e KAFKA_SERVER_URI=broker --network text_net  enricher

docker build -f .\persister\Dockerfile   -t persister .
docker run -d --name persister -e KAFKA_SERVER_URI=broker -e MONGO_HOST=mongodb  --network text_net  persister

docker build -f .\dataretrieval\Dockerfile   -t dataretrieval .
docker run -d --name dataretrieval -e MONGO_HOST=mongodb  --network text_net  -p 8200:8111  dataretrieval