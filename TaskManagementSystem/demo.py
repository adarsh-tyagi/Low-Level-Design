from TaskManagementSystem import TaskManagementSystem
from TaskPriority import TaskPriority
from TaskStatus import TaskStatus
from datetime import date
from TaskSortStrategy import SortByDueDate


class Demo:
    @staticmethod
    def main():
        task_management_system = TaskManagementSystem.get_instancce()
        
        user = task_management_system.create_user("Adarsh", "adarsh@example.com")
        
        task_list = task_management_system.create_task_list("Features")
        
        task = task_management_system.create_task("New feature", 
                                                  "Create new CRUD operations APIs", 
                                                  date.today().replace(day=date.today().day+2), 
                                                  TaskPriority.MEDIUM, user.id)
        
        subtask = task_management_system.create_task("Documentation", 
                                                  "Design request response contract document", 
                                                  date.today().replace(day=date.today().day+1), 
                                                  TaskPriority.HIGH, user.id)
        
        task.add_subtask(subtask)
        
        task_list.add_task(task)
        
        task_list.display()
        
        subtask.start_progress()
        
        search_result = task_management_system.search_tasks("feature", SortByDueDate())
        for task in search_result:
            print(task.get_title())
            

if __name__ == "__main__":
    Demo.main()