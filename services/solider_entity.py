import uuid

class SoliderCol:
    """_summary_
    """
    def __init__(self,first_name:str,last_name:str,phone_number:str,rank:str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.rank = rank
        self.id = uuid.uuid4()

    def return_solider(self)-> dict:
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone_number": self.phone_number,
            "rank": self.rank
        }
