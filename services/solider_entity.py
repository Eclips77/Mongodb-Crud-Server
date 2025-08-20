from typing import Optional
from uuid import uuid4

class Document:
    """
    Document class representing a document with personal information
    """
    
    def __init__(self, first_name: Optional[str] =  None, last_name: Optional[str] =  None, phone_number: Optional[str] =  None, rank: Optional[str] =  None, doc_id: Optional[str] = None):
        """
        Initialize a new Document instance
        
        Args:
            first_name (str): First name of the person
            last_name (str): Last name of the person
            phone_number (str): Phone number
            rank (str): Rank of the person
            doc_id (Optional[str]): Document ID, auto-generated if not provided
        """
        self.id = doc_id if doc_id else str(uuid4())
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.rank = rank

    def to_dict(self) -> dict:
            """
            Convert document to dictionary format
            
            Returns:
                dict: Document as dictionary
            """
            return {
                "_id": self.id,
                "first_name": self.first_name,
                "last_name": self.last_name,
                "phone_number": self.phone_number,
                "rank": self.rank
            } 
    
    @classmethod
    def from_dict(cls, data: dict):
        """
        Create Document instance from dictionary
        
        Args:
            data (dict): Dictionary containing document data
            
        Returns:
            Document: New Document instance
        """
        return cls(
            first_name=data.get("first_name"),
            last_name=data.get("last_name"),
            phone_number=data.get("phone_number"),
            rank=data.get("rank"),
            doc_id=data.get("_id")
        )      