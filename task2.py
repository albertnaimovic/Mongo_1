# Write a data population script. The script/function should create a document,
# with necessary fields. Values should be auto generated (random number/numbers, int, float, random words etcs.)
# and itteration=0 value how many documents we want to populate the DB.
# For the beggining lets agree that we want to create a database people, with collection
# employees . Fields: name,surname,age,years employed.

from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection
from typing import Dict
import random, names


def connect_to_mongodb(host: str, port: int, db_name: str) -> Database:
    client = MongoClient(host, port)
    database = client[db_name]
    return database


def insert_document(collection: Collection, document: Dict) -> str:
    result = collection.insert_one(document)
    return str(result.inserted_id)


# Example usage
if __name__ == "__main__":
    # Connection details
    mongodb_host = "localhost"
    mongodb_port = 27017
    database_name = "persons"
    collection_name = "employees_night_shift"

    # Connect to MongoDB
    db = connect_to_mongodb(mongodb_host, mongodb_port, database_name)

    # Retrieve a specific collection
    collection = db[collection_name]

    for _ in range(200):
        # Create (Insert) Operation
        document = {
            "name": names.get_first_name(),
            "surname": names.get_last_name(),
            "age": random.randint(18, 65),
            "years employed": random.randint(0, 10),
        }
        inserted_id = insert_document(collection, document)
        print(f"Employee added: {document['name']} {document['surname']}")
