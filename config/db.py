from pymongo import MongoClient

MONGO_URI = ""

db = MongoClient(MONGO_URI)

conn = db['']