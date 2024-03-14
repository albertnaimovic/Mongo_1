from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection
from typing import Dict, List


class MongoCRUD:
    def __init__(
        self, host: str, port: int, database_name: str, collection_name: str
    ) -> None:
        self.host = host
        self.port = port
        self.database_name = database_name
        self.collection = self.__connect_to_mongodb()[collection_name]

    def __connect_to_mongodb(self) -> Database:
        client = MongoClient(self.host, self.port)
        database = client[self.database_name]
        return database

    def find_documents(self, query: Dict) -> List[Dict]:
        documents = self.collection.find(query, {"_id": 0})
        return list(documents)

    def insert_one_document(self, document: Dict) -> str:
        result = self.collection.insert_one(document)
        return str(result.inserted_id)

    def insert_many_documents(self, document: Dict) -> str:
        result = self.collection.insert_many(document)
        return str(result.inserted_ids)

    def update_one_document(self, query: Dict, update: Dict) -> int:
        result = self.collection.update_one(query, {"$set": update})
        return result.modified_count

    def update_many_documents(self, query: Dict, update: Dict) -> int:
        result = self.collection.update_many(query, {"$set": update})
        return result.modified_count

    def delete_one_document(self, query: Dict) -> int:
        result = self.collection.delete_one(query)
        return result.deleted_count

    def delete_many_documents(self, query: Dict) -> int:
        result = self.collection.delete_many(query)
        return result.deleted_count

    def find_equal(self, key: str, value: int, parameters={}) -> List[Dict]:
        query = {key: {"$eq": value}}
        documents = self.collection.find(query, parameters)
        return list(documents)

    def find_greater_than(self, key: str, value: int, parameters={}) -> List[Dict]:
        query = {key: {"$gt": value}}
        documents = self.collection.find(query, parameters)
        return list(documents)

    def find_greater_or_equal(self, key: str, value: int, parameters={}) -> List[Dict]:
        query = {key: {"$gte": value}}
        documents = self.collection.find(query, parameters)
        return list(documents)

    def find_specified_values(
        self, key: str, values_list: list, parameters={}
    ) -> List[Dict]:
        query = {key: {"$in": values_list}}
        documents = self.collection.find(query, parameters)
        return list(documents)

    def find_less_than(self, key: str, value: int, parameters={}) -> List[Dict]:
        query = {key: {"$lt": value}}
        documents = self.collection.find(query, parameters)
        return list(documents)

    def find_less_or_equal(self, key: str, value: int, parameters={}) -> List[Dict]:
        query = {key: {"$lte": value}}
        documents = self.collection.find(query, parameters)
        return list(documents)

    def find_not_equal(self, key: str, value: int, parameters={}) -> List[Dict]:
        query = {key: {"$ne": value}}
        documents = self.collection.find(query, parameters)
        return list(documents)

    def find_all_instead_of(
        self, key: str, values_list: list, parameters={}
    ) -> List[Dict]:
        query = {key: {"$nin": values_list}}
        documents = self.collection.find(query, parameters)
        return list(documents)


database = MongoCRUD(
    host="localhost",
    port=27017,
    database_name="crud_class",
    collection_name="employees",
)


document = {
    "name": "Albert",
    "age": 45,
}
query = {}
update = {"age": 26}


print(database.find_greater_than(key="age", value=40, parameters={"_id": 0}))
