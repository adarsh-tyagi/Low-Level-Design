import threading
from datetime import date
import uuid
from User import User
from TaskPriority import TaskPriority
from TaskStatus import TaskStatus
from Comment import Comment
from ActivityLog import ActivityLog
from TaskState import TaskState, ToDoState
from TaskObserver import TaskObserver
from Tag import Tag


class Task:
    def __ini__(self, builder):
        self._id = builder._id
        self._title = builder._title
        self._description = builder._description
        self._due_date = builder._due_date
        self._priority = builder._priority
        self._created_by = builder._created_by
        self._assignee = builder._assignee
        self._tags = builder._tags
        self._current_state = ToDoState()
        self._comments = []
        self._subtasks = []
        self._activity_logs = []
        self._observers = []
        self._lock = threading.Lock()
        self.add_log(f"Task created with title: {self._title}")
    
    def set_assignee(self, user):
        with self._lock:
            self._assignee = user
            self.add_log(f"Assigned to {user.name}")
            self.notify_observers("assigned")
    
    def update_priority(self, priority):
        with self._lock:
            self._priority = priority
            self.notify_observers("priority")
        
    def add_comment(self, comment):
        with self._lock:
            self._comments.append(comment)
            self.add_log(f"Comment added by {comment.author.name}")
            self.notify_observers("comment")
    
    def add_subtask(self, subtask):
        with self._lock:
            self._subtasks.append(subtask)
            self.add_log(f"Subtask added: {subtask.get_title()}")
            self.notify_observers("subtask_added")
    
    def set_state(self, state):
        self._current_state = state
        self.add_log(f"status updated to {state.get_status().value}")
        self.notify_observers("status")
    
    def start_progress(self):
        self._current_state.start_progress(self)
    
    def complete_task(self):
        self._current_state.complete_task(self)
    
    def reopen_ticket(self):
        self._current_state.reopen_ticket(self)
    
    def add_observer(self, observer):
        self._observers.append(observer)
    
    def remove_observer(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)
    
    def notify_observers(self, change_type):
        for observer in self._observers:
            observer.update(self, change_type)
    
    def add_log(self, log_description):
        self._activity_logs.append(ActivityLog(log_description))
    
    def is_composite(self):
        return len(self._subtasks) > 0

    def display(self, indent = ""):
        print(f"{indent} - {self._title} [{self.get_status().value}, {self._priority.value}, Due: {self._due_date}]")
        if self.is_composite():
            for subtask in self._subtasks:
                subtask.display(indent + " ")
    
    def get_id(self):
        return self._id
    
    def get_title(self):
        return self._title
    
    def get_description(self):
        return self._description
    
    def get_priority(self):
        return self._priority
    
    def get_due_date(self):
        return self._due_date
    
    def get_assignee(self):
        return self._assignee
    
    def get_title(self, title):
        self._title = title
        
    def set_description(self, description):
        self._description = description
        
    def get_status(self):
        return self._current_state.get_status()


    # builder pattern
    
    class TaskBuilder:
        def __init__(self, title):
            self._id = str(uuid.uuid4())
            self._title = title
            self._description = ""
            self._due_date = None
            self._priority = None
            self._created_by = None
            self._assignee = None
            self._tags = set()
            
        def description(self, description):
            self._description = description
            return self
            
        def due_date(self, due_date):
            self._due_date = due_date
            return self
        
        def priority(self, priority):
            self._priority = priority
            return self
        
        def assignee(self, assignee):
            self._assignee = assignee
            return self
        
        def created_by(self, created_by):
            self._created_by = created_by
            return self
        
        def tags(self, tags):
            self._tags = tags
            return self
        
        def build(self):
            return Task(self)