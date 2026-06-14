import uuid
from datetime import datetime
from User import User


class Comment:
    def __init__(self, content, author):
        self._id = str(uuid.uuid4())
        self._content = content
        self._author = author
        self._timestamp = datetime.now()
    
    @property
    def author(self):
        return self._author
    