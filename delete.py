from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection
from typing import Dict


def connect_to_mongodb(host: str, port: int, db_name: str) -> Database:
    client = MongoClient(host, port)
    database = client[db_name]
    return database


def delete_documents(collection: Collection, query: Dict) -> int:
    result = collection.delete_many(query)
    return result.deleted_count


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

    # Delete Operation
    query = {"name": "Joseph", "surname": "Whitaker"}
    deleted_count = delete_documents(collection, query)
    print(f"Deleted {deleted_count} documents")
