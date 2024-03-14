from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection
from typing import Dict


def connect_to_mongodb(host: str, port: int, db_name: str) -> Database:
    client = MongoClient(host, port)
    database = client[db_name]
    return database


def insert_document(collection: Collection, document: Dict) -> str:
    result = collection.insert_one(document)
    print(f"Result: {result}")
    return str(result.inserted_id)


# Example usage
if __name__ == "__main__":
    # Connection details
    mongodb_host = "localhost"
    mongodb_port = 27017
    database_name = "lesson1_database"
    collection_name = "lesson1_collection"

    # Connect to MongoDB
    db = connect_to_mongodb(mongodb_host, mongodb_port, database_name)

    # Retrieve a specific collection
    collection = db[collection_name]

    # Create (Insert) Operation
    document = {
        "name": "Jameson Doe",
        "age": 30,
        "email": "johndoe@example.com",
        "title": "Pavadinimaz",
    }
    inserted_id = insert_document(collection, document)
    print(f"Inserted document with ID: {inserted_id}")
