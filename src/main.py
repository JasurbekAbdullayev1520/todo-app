import sys
from .commands import (
    add_task,
    show_tasks,
    update_task,
    delete_task,
    completed_task
)


def main():
    while True:
        print("---menu----")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Completed")
        print("6. Exit")
        
        choice = input("Select option: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            completed_task()
        elif choice == "6":
            sys.exit()




        