docker network create kafkanet
docker run -d --name mongotry --network kafkanet mongo:latest

docker build -f .\retriever\Dockerfile   -t retriever .
docker run -d --name retriever retriever
docker build -f .\preprocessor\Dockerfile   -t preprocessor .
docker run -d --name preprocessor -e KAFKA_SERVER_URI=broker --network kafkanet  preprocessor
docker build -f .\enricher\Dockerfile   -t enricher .
docker run -d --name enricher -e KAFKA_SERVER_URI=broker --network kafkanet  enricher
docker build -f .\persister\Dockerfile   -t persister .
docker run -d --name persister -e KAFKA_SERVER_URI=broker --network kafkanet  persister
docker build -f .\dataretrieval\Dockerfile   -t dataretrieval .
docker run -d --name dataretrieval -e MONGO_HOST=mongotry  -e KAFKA_SERVER_URI=broker --network kafkanet  -p 8200:8111  dataretrieval