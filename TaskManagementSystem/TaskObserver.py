from abc import ABC, abstractmethod

class TaskObserver(ABC):
    @abstractmethod
    def update(self, task, change_type):
        pass
    
class ActivityLogger(TaskObserver):
    def update(self, task, change_type):
        print(f"LOGGER: TASK '{task.get_title()}' was updated. Change: {change_type}")