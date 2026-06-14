from datetime import datetime

class ActivityLog:
    def __init__(self, description):
        self._description = description
        self._timestamp = datetime.now()
        
    def __str__(self):
        return f"[{self._timestamp}] {self._description}"