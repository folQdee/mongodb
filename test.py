from pymongo import MongoClient
import key_param
print(MongoClient(key_param.mongodb_uri).admin.command("ping"))
