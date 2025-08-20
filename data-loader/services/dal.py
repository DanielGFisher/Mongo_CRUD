from pymongo import MongoClient
from soldier import Soldier
from typing import List

class SoldierDAL:
    def __init__(self, uri="mongodb://localhost:27017", db_name="enemySoldiers"):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db["soldier_details"]

    def get_all(self) -> List[dict]:
        return list(self.collection.find({}, {"_id": 0}))

    def insert(self, soldier: Soldier) -> dict:
        self.collection.insert_one(soldier.dict())
        return {"status": "success", "message": "Soldier inserted"}

    def update(self, soldier_id: int, field: str, value: str) -> dict:
        result = self.collection.update_one(
            {"ID": soldier_id}, {"$set": {field: value}}
        )
        if result.modified_count > 0:
            return {"status": "success", "message": "Soldier updated"}
        return {"status": "fail", "message": "No record updated"}

    def delete(self, soldier_id: int) -> dict:
        result = self.collection.delete_one({"ID": soldier_id})
        if result.deleted_count > 0:
            return {"status": "success", "message": "Soldier deleted"}
        return {"status": "fail", "message": "No record deleted"}
