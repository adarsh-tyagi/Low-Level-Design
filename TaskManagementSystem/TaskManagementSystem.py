import threading
from User import User
from Task import Task
from TaskList import TaskList
from TaskPriority import TaskPriority
from TaskStatus import TaskStatus
from TaskSortStrategy import TaskSortStrategy
from TaskObserver import ActivityLogger
from datetime import date


class TaskManagementSystem:
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._initialized = False
        return cls._instance
    
    
    def __init__(self):
        if not self.__initialized:
            self._users = {}
            self._tasks = {}
            self._task_lists = {}
            self._initialized = True
            
    @classmethod
    def get_instance(cls):
        return cls()
    
    def create_user(self, name, email):
        user = User(name, email)
        self._users[user.id] = user
        return user
    
    def create_task_list(self, list_name):
        task_list = TaskList(list_name)
        self._task_lists[task_list.id] = task_list
        return task_list

    def create_task(self, title, description, due_date, priority, created_by_user_id):
        created_by = self._users.get(created_by_user_id)
        if created_by is None:
            raise ValueError("User not found")
    
        task = Task.TaskBuilder(title).description(description).due_date(due_date).priority(priority).created_by(created_by).build()
        task.add_observer(ActivityLogger)
        self._tasks[task.get_id()] = task
        return task
    
    def list_tasks_by_user(self, user_id):
        user = self._users.get(user_id)
        return [task for task in self._tasks.values() if task.get_assignee() == user]
    
    def list_tasks_by_status(self, status):
        return [task for task in self._tasksk.values() if task.get_status() == status]
    
    def delete_task(self, task_id):
        if task_id in self._tasks:
            del self._tasks[task_id]
    
    def search_tasks(self, keyword, sorting_strategy):
        matching_tasks = []
        for task in self._tasks.values():
            if (keyword in task.get_title() or keyword in task.get_description()):
                matching_tasks.append(task)
        
        sorting_strategy.sort(matching_tasks)
        return matching_tasks