from pymongo import MongoClient

class ConexionMongo():
    def __init__(self):
        self.client = MongoClient(host='test_mongodb',
                            port=27017, 
                            username='root', 
                            password='pass',
                            authSource="admin")
        self.db = self.client["bd_trivia"]
    def connect_mongo(self):
        return self.db