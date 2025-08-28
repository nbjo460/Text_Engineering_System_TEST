import fastapi
import config
from utils.mongodb_tools.DAL_mongodb import DAL_mongo as Dal

app = fastapi.FastAPI()



@app.get("/")
def root():
    return {"status" : "HELLO"}
@app.get("/get-messages-antisemitic")
def load_interesting():
    """
    In route: "/get-interesting", load the messages.
    :return: json
    """

    dal = Dal(config.MONGO_PREFIX,
              config.MONGO_HOST,
              config.MONGO_DB,
              config.MONGO_COLLECTION_ANTISEMITIC)
    return dal.get_all_documents()

@app.get("/get-messages-not-antisemitic")
def load_interesting():
    """
    In route: "/get-interesting", load the messages.
    :return: json
    """

    dal = Dal(config.MONGO_PREFIX,
              config.MONGO_HOST,
              config.MONGO_DB,
              config.MONGO_COLLECTION_NOT_ANTISEMITIC)
    return dal.get_all_documents()
