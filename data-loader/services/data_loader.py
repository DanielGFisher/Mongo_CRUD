from fastapi import FastAPI
from dal import SoldierDAL
from soldier import Soldier

app = FastAPI(title="Enemy Soldiers API")
dal = SoldierDAL(uri="mongodb://mongo:27017")

@app.get("/soldiersdb/")
def get_soldiers():
    return dal.get_all()

@app.post("/soldiersdb/")
def add_soldier(soldier: Soldier):
    return dal.insert(soldier)

@app.put("/soldiersdb/{soldier_id}")
def update_soldier(soldier_id: int, field: str, value: str):
    return dal.update(soldier_id, field, value)

@app.delete("/soldiersdb/{soldier_id}")
def delete_soldier(soldier_id: int):
    return dal.delete(soldier_id)
