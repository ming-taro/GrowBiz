import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()


class MongoDBConnector:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(MongoDBConnector, cls).__new__(cls)
            cls._client = MongoClient(os.getenv("MONGO_URI"))
            cls._db = cls._client[os.getenv("MONGO_DB_NAME")]
        return cls._instance

    def get_db(self):
        return self._db

    def get_collection(self, collection_name):
        return self._db[collection_name]
