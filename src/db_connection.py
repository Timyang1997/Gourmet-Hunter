from pymongo import MongoClient
from pymongo.server_api import ServerApi

MONGO_URI = "mongodb+srv://gournet:Hunter@gourmethunter.ena0eso.mongodb.net/?retryWrites=true&w=majority&appName=GourmetHunter"

client = MongoClient(MONGO_URI, server_api=ServerApi('1'))

database = client.get_database("gourmet_hunter")

