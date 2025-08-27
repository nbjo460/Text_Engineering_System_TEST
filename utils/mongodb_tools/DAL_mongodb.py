from pymongo import MongoClient



class DAL_mongo:

    def __init__(self, prefix, host, database, collection, user= None, password= None):
        self.prefix = prefix
        self.host = host
        self.database = database
        self.collection = collection
        self.user = user
        self.password = password
        self.URI = self.get_URI()
        self.client = None


    def get_URI(self):
        if self.user and self.password:
            URI = f"{self.prefix}://{self.user}:{self.password}@{self.host}::27017"
        else:
            URI = f"{self.prefix}://{self.host}:27017"

        return URI


    def open_connection(self):
        try:
            self.client = MongoClient(self.URI)
            self.client.admin.command("ping")
            return True
        except Exception as e:
            self.client = None
            print("Error: ", e)
            return False


    def get_documents(self, num_skip=None, num_limit=None, sort_by_filed=None):
        if self.client:
            db = self.client[self.database]
            collection = db[self.collection]

            if num_skip is not None and num_limit is not None and sort_by_filed is not None:
                data = collection.find({}, {"_id": 0}).skip(num_skip).limit(num_limit).sort({sort_by_filed: 1})
            elif num_skip is not None and num_limit is not None:
                data = collection.find({}, {"_id": 0}).skip(num_skip).limit(num_limit)
            else:
                 data = collection.find({}, {"_id": 0})

            return list(data)



    def insert_one(self, data):
        if self.client:
            db = self.client[self.database]
            collection = db[self.collection]
            results = collection.insert_one(data)
            return results


    def close_connection(self):
        if self.client:
            self.client.close()


if __name__ == "__main__":
    DAL_mongo = DAL_mongo(prefix="mongodb+srv",
                          host="cluster0.6ycjkak.mongodb.net/",
                          database="IranMalDB",
                          collection="tweets",
                          user="IRGC_NEW",
                          password="iran135")
    DAL_mongo.open_connection()
    documents = DAL_mongo.get_documents(5, 5, "CreateDate")
    print(documents[0].keys())
    print(type(documents[0]['CreateDate']))
    DAL_mongo.close_connection()