from abc import ABC, abstractmethod
from Task import Task
from TaskPriority import TaskPriority
from datetime import date

class TaskSortStrategy(ABC):
    @abstractmethod
    def sort(self, tasks):
        pass
    
class SortByPriority(TaskSortStrategy):
    def sort(self, tasks):
        priority_order = {TaskPriority.CRITICAL: 4, TaskPriority.HIGH: 3,
                          TaskPriority.MEDIIUM: 2, TaskPriority.LOW: 1}
        tasks.sort(key=lambda task: priority_order.get(task.get_priority(), 0), reverse=True)

class SortByDueDate(TaskSortStrategy):
    def sort(self, tasks):
        tasks.sort(key=lambda task: task.get_due_date() if task.get_due_date() else date.max)