import threading
import uuid
from Task import Task

class TaskList:
    def __init__(self, name):
        self._id = str(uuid.uuid4())
        self._name = name
        self._tasks = []
        self._lock = threading.Lock()
    
    def add_task(self, task):
        with self._lock:
            self._tasks.append(task)
    
    def get_tasks(self):
        with self._lock:
            return self._tasks.copy()
    
    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name
    
    def display(self):
        print(f"-- Task List: {self._name} --")
        for task in self._tasks:
            task.display("")
        print("-"*25)