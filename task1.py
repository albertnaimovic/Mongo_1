# 1. Create a CLI application that takes name surname gender and age (in a single sentence).
# Check if gender or age is provided correctly. Result save to database with timestamp of the event.

from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection
from typing import Dict
from datetime import datetime


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
    database_name = "task1_database"
    collection_name = "task1_collection"

    # Connect to MongoDB
    db = connect_to_mongodb(mongodb_host, mongodb_port, database_name)

    # Retrieve a specific collection
    collection = db[collection_name]

    person_info = (
        input("Enter your name, surname, gender, and age: ").replace(" ", "").split(",")
    )

    name = person_info[0]
    surname = person_info[1]
    gender = person_info[2]
    age = person_info[3]

    if gender.lower() in ["male", "female"] and age.isnumeric():

        document = {
            "name": name,
            "surname": surname,
            "gender": gender,
            "age": int(age),
            "createdAt": datetime.now(),
        }
        inserted_id = insert_document(collection, document)
        print(f"{', '.join(person_info)} have been inserted")
    else:
        print("You've entered wrong gender or age")
