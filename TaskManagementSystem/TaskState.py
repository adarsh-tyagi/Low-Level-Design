from abc import ABC, abstractmethod
from TaskStatus import TaskStatus
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Task import Task
    
class TaskState(ABC):
    @abstractmethod
    def start_progress(self, task):
        pass
    
    @abstractmethod
    def complete_task(self, task):
        pass
    
    @abstractmethod
    def reopen_ticket(self, task):
        pass
    
    @abstractmethod
    def get_status(self):
        pass
    
class ToDoState(TaskState):
    def start_progress(self, task):
        task.set_state(InProgressState())
    
    def complete_task(self, task):
        print("Can not complete task which is not in progress")
    
    def reopen_ticket(self, task):
        print("Task is alredy in todo state")
    
    def get_status(self):
        return TaskStatus.TODO

class InProgressState(TaskState):
    def start_progress(self, task):
        print("Alredy in progress")
    
    def complete_task(self, task):
        task.set_state(DoneState())
    
    def reopen_ticket(self, task):
        task.set_state(ToDoState())
    
    def get_status(self):
        return TaskStatus.IN_PROGRESS

class DoneState(TaskState):
    def start_progress(self, task):
        print("Can not start completed task, reopen it first")
    
    def complete_task(self, task):
        print("Already done")
    
    def reopen_ticket(self, task):
        task.set_state(ToDoState())
    
    def get_status(self):
        return TaskStatus.DONE