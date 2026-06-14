import uuid

class User:
    def __init__(self, name: str, email: str):
        self._id = str(uuid.uuid4())
        self.name = name
        self.email = email
    
    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self.name
    
    @property
    def email(self):
        return self.email
    