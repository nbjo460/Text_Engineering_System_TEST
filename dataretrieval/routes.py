import fastapi
from contextlib import asynccontextmanager
import config
from utils.mongodb_tools.DAL_mongodb import DAL_mongo as Dal

dal_NOT_ANTISEMITIC = Dal(config.MONGO_PREFIX,
                           config.MONGO_HOST,
                           config.MONGO_DB,
                           config.MONGO_COLLECTION_NOT_ANTISEMITIC)

dal_ANTISEMITIC = Dal(config.MONGO_PREFIX,
          config.MONGO_HOST,
          config.MONGO_DB,
          config.MONGO_COLLECTION_ANTISEMITIC)

@asynccontextmanager
async def lifespan(app: fastapi.FastAPI):
    dal_ANTISEMITIC.open_connection()
    dal_NOT_ANTISEMITIC.open_connection()
    yield
    dal_ANTISEMITIC.close_connection()
    dal_NOT_ANTISEMITIC.close_connection()


app = fastapi.FastAPI(lifespan=lifespan)




@app.get("/")
def root():
    return {"status" : "HELLO"}


@app.get("/get-messages-antisemitic")
def load_interesting():
    """
    In route: "/get-interesting", load the messages.
    :return: json
    """

    return dal_ANTISEMITIC.get_all_documents()

@app.get("/get-messages-not-antisemitic")
def load_interesting():
    """
    In route: "/get-interesting", load the messages.
    :return: json
    """

    return dal_NOT_ANTISEMITIC.get_all_documents()
