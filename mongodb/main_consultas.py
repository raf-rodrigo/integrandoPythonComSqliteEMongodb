from pprint import pprint

import pymongo as pyM
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://rafrodrigo:YNWAq6EvhXn52UHZ@cluster0.nt3vlbe.mongodb.net/?retryWrites=true&w=majority"
client = pyM.MongoClient(uri)
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client.clients
collection = db.banco
#
# pprint(collection.find())
# find = collection.find()
# for ver in find:
#     pprint(ver)
#
# pprint(db.banco.find_one())

# pprint(db.banco.find())

