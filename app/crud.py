from typing import Any, Dict, List
from pymongo.collection import Collection

class AlunoCRUD:
    def __init__(self, collection: Collection) -> None:
        self.c = collection

    # CREATE
    def create(self, data: Dict[str, Any]) -> str:
        res = self.c.insert_one(data)
        return str(res.inserted_id)

    # READ (todos)
    def read_all(self) -> List[Dict[str, Any]]:
        return list(self.c.find())

    # READ (por filtro)
    def read(self, filtro: Dict[str, Any]) -> List[Dict[str, Any]]:
        return list(self.c.find(filtro))

    # UPDATE (update_many para exemplo)
    def update(self, filtro: Dict[str, Any], updates: Dict[str, Any]) -> int:
        res = self.c.update_many(filtro, {"$set": updates})
        return res.modified_count

    # DELETE (delete_many para exemplo)
    def delete(self, filtro: Dict[str, Any]) -> int:
        res = self.c.delete_many(filtro)
        return res.deleted_count
