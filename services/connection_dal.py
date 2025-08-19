from http import client
from pymongo import MongoClient
from typing import Dict, List, Any, Optional


class ConnectionDal:
    def __init__(self,connection:str,db_name:str):
        self.client = MongoClient(connection)
        self.db = self.client[db_name]