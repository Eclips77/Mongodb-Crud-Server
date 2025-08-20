from typing import Optional
from uuid import uuid4

class Soldier:
    """
    Soldier entity class
    """
    
    def __init__(self, first_name: Optional[str] = None, last_name: Optional[str] = None, 
                 phone_number: Optional[str] = None, rank: Optional[str] = None, soldier_id: Optional[str] = None):
        """
        Initialize a new Soldier instance
        
        Args:
            first_name (str): שם פרטי
            last_name (str): שם משפחה
            phone_number (str): מספר טלפון
            rank (str): דרגה
            soldier_id (str): מזהה חייל
        """
        self.id = soldier_id if soldier_id else str(uuid4())
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.rank = rank

    def to_dict(self) -> dict:
        """
        Convert soldier to dictionary format
        
        Returns:
            dict: Soldier as dictionary
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
        Create Soldier instance from dictionary
        
        Args:
            data (dict): Dictionary containing soldier data
            
        Returns:
            Soldier: New Soldier instance
        """
        return cls(
            first_name=data.get("first_name"),
            last_name=data.get("last_name"),
            phone_number=data.get("phone_number"),
            rank=data.get("rank"),
            soldier_id=data.get("_id")
        )

    def __str__(self) -> str:
        """String representation of soldier"""
        return f"Soldier(id={self.id}, name={self.first_name} {self.last_name}, rank={self.rank})"      