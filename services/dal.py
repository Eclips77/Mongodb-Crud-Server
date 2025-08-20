
from typing import List, Optional
from services.connection_dal import DatabaseConnection
from services.solider_entity import Document
import config

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
            result = self.collection.find_one({"_id": doc_id})
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
                {"_id": doc_id},
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
            result = self.collection.delete_one({"_id": doc_id})
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
            results = self.collection.find()
            return [Document.from_dict(doc) for doc in results]
        except Exception as e:
            print(f"Error getting all documents: {e}")
            return []
    
    def main_operations(self, operation: str, **kwargs):
        """
        Main method to handle all CRUD operations
        
        Args:
            operation (str): Operation type ('create', 'read', 'update', 'delete', 'get_all')
            **kwargs: Operation-specific parameters
            
        Returns:
            Operation result
        """
        operations = {
            'create': lambda: self.create(kwargs.get('document')),
            'read': lambda: self.read(kwargs.get('doc_id')),
            'update': lambda: self.update(kwargs.get('doc_id'), kwargs.get('update_data')),
            'delete': lambda: self.delete(kwargs.get('doc_id')),
            'get_all': lambda: self.get_all()
        }
        
        if operation in operations:
            return operations[operation]()
        else:
            raise ValueError(f"Unknown operation: {operation}")
    
    def close_connection(self):
        """
        Close database connection
        """
        self.db_connection.disconnect()
