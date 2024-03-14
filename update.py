from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection
from typing import Dict


def connect_to_mongodb(host: str, port: int, db_name: str) -> Database:
    client = MongoClient(host, port)
    database = client[db_name]
    return database


def update_document(collection: Collection, query: Dict, update: Dict) -> int:
    result = collection.update_many(query, {"$set": update})
    return result.modified_count


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

    # Update Operation
    query = {"name": "Joseph"}
    update = {"age": 40}
    modified_count = update_document(collection, query, update)
    print(f"Modified {modified_count} documents")
