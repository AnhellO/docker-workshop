import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

print("##### RECORDS #####")
for hooman in client["mi-db"].hoomans.find():
    print(hooman)