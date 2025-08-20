from typing import List, Optional, Dict, Any
from pymongo.collection import Collection
from services.connection_dal import DatabaseConnection
from services.solider_entity import Soldier
from services import config

class SoldierDAL:
    """
    Data Access Layer for Soldier entity - פשוט ויעיל
    """
    
    def __init__(self):
        """Initialize DAL with database connection"""
        self.db_connection = DatabaseConnection()
        self.db = self.db_connection.connect()
        self.collection: Collection = self.db[config.MONGODB_COLLECTION]

    def create(self, soldier: Soldier) -> str:
        """
        Create new soldier - יצירת חייל חדש
        
        Args:
            soldier (Soldier): Soldier object to create
            
        Returns:
            str: ID of created soldier
        """
        try:
            soldier_dict = soldier.to_dict()
            result = self.collection.insert_one(soldier_dict)
            return str(result.inserted_id)
        except Exception as e:
            raise Exception(f"Failed to create soldier: {e}")

    def get_by_id(self, soldier_id: str) -> Optional[Soldier]:
        """
        Get soldier by ID - קבלת חייל לפי מזהה
        
        Args:
            soldier_id (str): Soldier ID
            
        Returns:
            Optional[Soldier]: Soldier object or None
        """
        try:
            result = self.collection.find_one({"_id": soldier_id})
            if result:
                return Soldier.from_dict(result)
            return None
        except Exception as e:
            raise Exception(f"Failed to get soldier: {e}")

    def get_all(self) -> List[Soldier]:
        """
        Get all soldiers - קבלת כל החיילים
        
        Returns:
            List[Soldier]: List of all soldiers
        """
        try:
            results = self.collection.find()
            return [Soldier.from_dict(doc) for doc in results]
        except Exception as e:
            raise Exception(f"Failed to get soldiers: {e}")

    def update(self, soldier_id: str, update_data: Dict[str, Any]) -> bool:
        """
        Update soldier - עדכון חייל
        
        Args:
            soldier_id (str): Soldier ID
            update_data (Dict): Data to update
            
        Returns:
            bool: True if updated successfully
        """
        try:
            # Remove _id from update data if exists
            update_data.pop("_id", None)
            
            result = self.collection.update_one(
                {"_id": soldier_id},
                {"$set": update_data}
            )
            return result.modified_count > 0
        except Exception as e:
            raise Exception(f"Failed to update soldier: {e}")

    def delete(self, soldier_id: str) -> bool:
        """
        Delete soldier - מחיקת חייל
        
        Args:
            soldier_id (str): Soldier ID
            
        Returns:
            bool: True if deleted successfully
        """
        try:
            result = self.collection.delete_one({"_id": soldier_id})
            return result.deleted_count > 0
        except Exception as e:
            raise Exception(f"Failed to delete soldier: {e}")

    def search_by_name(self, name: str) -> List[Soldier]:
        """
        Search soldiers by name - חיפוש חיילים לפי שם
        
        Args:
            name (str): Name to search for
            
        Returns:
            List[Soldier]: List of matching soldiers
        """
        try:
            # Search in both first_name and last_name
            query = {
                "$or": [
                    {"first_name": {"$regex": name, "$options": "i"}},
                    {"last_name": {"$regex": name, "$options": "i"}}
                ]
            }
            results = self.collection.find(query)
            return [Soldier.from_dict(doc) for doc in results]
        except Exception as e:
            raise Exception(f"Failed to search soldiers: {e}")

    def get_by_rank(self, rank: str) -> List[Soldier]:
        """
        Get soldiers by rank - קבלת חיילים לפי דרגה
        
        Args:
            rank (str): Rank to filter by
            
        Returns:
            List[Soldier]: List of soldiers with specified rank
        """
        try:
            results = self.collection.find({"rank": rank})
            return [Soldier.from_dict(doc) for doc in results]
        except Exception as e:
            raise Exception(f"Failed to get soldiers by rank: {e}")

    def count(self) -> int:
        """
        Count total soldiers - ספירת חיילים
        
        Returns:
            int: Total number of soldiers
        """
        try:
            return self.collection.count_documents({})
        except Exception as e:
            raise Exception(f"Failed to count soldiers: {e}")
