from pymongo import MongoClient
from pymongo.database import Database
from services import config

class DatabaseConnection:
    """
    MongoDB connection manager
    """
    
    def __init__(self):
        """
        Initialize database connection
        """
        self.client = None
        self.database = None
    
    def connect(self) -> Database:
        """
        Establish connection to MongoDB
        
        Returns:
            Database: MongoDB database instance
        """
        try:
            self.client = MongoClient(config.MONGODB_HOST, config.MONGODB_PORT)
            self.database = self.client[config.MONGODB_DATABASE]
            return self.database
        except Exception as e:
            raise ConnectionError(f"Failed to connect to MongoDB: {e}")
    
    def disconnect(self):
        """
        Close database connection
        """
        if self.client:
            self.client.close()
    
    def test_connection(self) -> bool:
        """
        Test database connection
        
        Returns:
            bool: True if connection is successful
        """
        try:
            if self.database is None:
                self.connect()
            # Test connection by pinging the database
            if self.database is not None:
                self.database.command('ping')
                return True
            return False
        except Exception:
            return False