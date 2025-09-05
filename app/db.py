import os
from pymongo import MongoClient

def get_client():
    """Retorna um cliente MongoDB usando MONGO_URI (ou localhost por padrão)."""
    uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
    return MongoClient(uri)

def get_collection(db_name: str = "escola", coll_name: str = "alunos"):
    client = get_client()
    db = client[db_name]
    return db[coll_name]
