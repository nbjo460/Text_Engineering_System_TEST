from kafka_tools.producer import Producer
from mongodb_tools.DAL_mongodb import DAL_mongo


class Retriever:

    def __init__(self, DAL_mongo: DAL_mongo,
                 num_documents: int = None, sort_by_field: str = None):

        self.DAL_mongo = DAL_mongo
        self.num_limit = num_documents
        self.num_skip = num_documents
        self.sort_by_field = sort_by_field



    def get_next_documents(self):
        if isinstance(self.DAL_mongo, DAL_mongo):
            connect = self.DAL_mongo.open_connection()
            if connect:
                documents = self.DAL_mongo.get_documents(num_skip=self.num_skip,
                                                              num_limit=self.num_limit,
                                                              sort_by_filed=self.sort_by_field)

                self.DAL_mongo.close_connection()
                return documents