from typing import List, Optional
from services.connection_dal import DatabaseConnection
from services.solider_entity import Document
from services import config

class DocumentDAL:
    """
    Data Access Layer for Document CRUD operations
    """
    
    def __init__(self):
        """
        Initialize DAL with database connection
        """
        self.db_connection = DatabaseConnection()
        self.database = self.db_connection.connect()
        self.collection = self.database[config.MONGODB_COLLECTION]
    
    def create(self, document: Document) -> bool:
        """
        Create a new document in the database
        
        Args:
            document (Document): Document to create
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            result = self.collection.insert_one(document.to_dict())
            return result.acknowledged
        except Exception as e:
            print(f"Error creating document: {e}")
            return False
    
    def read(self, doc_id: str) -> Optional[Document]:
        """
        Read a document by ID
        
        Args:
            doc_id (str): Document ID to search for
            
        Returns:
            Optional[Document]: Document if found, None otherwise
        """
        try:
            result = self.collection.find_one({"id": doc_id})
            if result:
                return Document.from_dict(result)
            return None
        except Exception as e:
            print(f"Error reading document: {e}")
            return None
    
    def update(self, doc_id: str, update_data: dict) -> bool:
        """
        Update a document by ID
        
        Args:
            doc_id (str): Document ID to update
            update_data (dict): Data to update
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            result = self.collection.update_one(
                {"id": doc_id},
                {"$set": update_data}
            )
            return result.modified_count > 0
        except Exception as e:
            print(f"Error updating document: {e}")
            return False
    
    def delete(self, doc_id: str) -> bool:
        """
        Delete a document by ID
        
        Args:
            doc_id (str): Document ID to delete
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            result = self.collection.delete_one({"id": doc_id})
            return result.deleted_count > 0
        except Exception as e:
            print(f"Error deleting document: {e}")
            return False
    
    def get_all(self) -> List[Document]:
        """
        Get all documents from the database
        
        Returns:
            List[Document]: List of all documents
        """
        try:
            results = self.collection.find({},{"_id":0})
            return [Document.from_dict(doc) for doc in results]
        except Exception as e:
            print(f"Error getting all documents: {e}")
            return []
    
    def close_connection(self):
        """
        Close database connection
        """
        self.db_connection.disconnect()
