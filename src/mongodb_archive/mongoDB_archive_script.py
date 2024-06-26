from configparser import ConfigParser
from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime, timedelta

# get api key from config file and get data from AirTabe
config = ConfigParser()

config.read("../../config/config.ini")
dbConnectionString = config.get("default", "mongo_db_write")

client = MongoClient(dbConnectionString)
print("Connected to DB.")
problem = client.pagesuccess.problem

print("Fetched the problem collection.")

problemCount = problem.count_documents({})
print("Size before removal:")
print(problemCount)

# Archive documents older than...
N_DAYS_AGO = 100

today = datetime.now()
n_days_ago = today - timedelta(days=N_DAYS_AGO)
n_days_ago = n_days_ago.strftime("%Y-%m-%d")
print(n_days_ago)

myquery = {"problemDate": {"$lte": n_days_ago}}

counter = 0
batch_size = 1000
deleted_count = batch_size

while deleted_count == batch_size:
    batch = problem.find(myquery, {"_id": 1}).limit(batch_size)
    deleted_count = 0
    for doc in batch:
        problem.delete_one({"_id": doc["_id"]})
        deleted_count += 1
        counter += 1
        print("Deleted so far: " + str(counter))

print("Entries Deleted: " + str(counter))

problemCount = problem.count_documents({})
print("Size after removal:")
print(problemCount)
