from datetime import datetime

from rich.console import Console
from rich.table import Table

from .storage import (
    create_task,
    get_tasks,
    save_database,
    read_database,
)


def add_task():
    name = input("Task name: ").strip().capitalize()
    description = input("Description: ").strip().capitalize()
    category = input("Category: ").strip().title()
    due_date = input("Date (example: 2025-10-11): ")

    due_date = datetime.strptime(due_date, "%Y-%m-%d")
    if due_date < datetime.now():
        print("Date shoulde be greater than or equal to now.")
        return

    create_task(name, description, category, due_date)
    print("✅ Vazifa muvaffaqiyatli qo'shildi!")


def show_tasks():
    tasks = get_tasks()

    console = Console()

    table = Table(title="All Tasks")
    table.add_column("Number")
    table.add_column("Name")
    table.add_column("Category")
    table.add_column("Due Date")

    for num, task in enumerate(tasks, start=1):
        du_date = task["due_date"].strftime("%d/%m/%Y")
        table.add_row(str(num), task["name"], task["category"], du_date)
    
    console.print(table)

    num = int(input("Task detail: "))
    task = tasks[num - 1]
    
    status = "❌Incompleted"
    if task["status"]:
        status = "✅ Completed"
    du_date = task["due_date"].strftime("%d/%m/%Y")
    created_date = task["created_date"].strftime("%d/%m/%Y, %H:%M:%S")

    print(f"Task name: {task['name']}")
    print(f"Description: {task['description']}")
    print(f"Category: {task['category']}")
    print(f"Status: {status}")
    print(f"Due Date: {du_date}")
    print(f"Created Date: {created_date}")
    
    print()

def update_task():
    tasks = read_database()
    r = int(input("O'zgartirmoqchi bo'gan task ID sini kiriting: "))
    for task in tasks:
        if task["id"] == r:
            new_name = input("Yangi nom: ")
            task["name"] = new_name or task["name"]

            new_description = input("Yangi description: ")
            task["description"] = new_description or task["description"]

            new_category = input("Yangi category: ")
            task["category"] = new_category or task["category"]

            save_database(tasks)
            print("Task muvaffaqiyatli o'zgartirildi!")
            return tasks 
        
def delete_task():
    tasks = read_database()
    r = int(input("O'chirmoqchi bo'lgan task ID sini kiriting: "))
    for task in tasks:
        if task["id"] == r:
            tasks.remove(task)
            save_database(tasks)
            print("Task muvaffaqiyatli o'chirildi!")
            return tasks
        
def completed_task():
    tasks = read_database()
    r = int(input("Statusni o'zgartirmoqchi bo'lgan task ID sini kiriting: "))
    for task in tasks:
        if task["id"] == r:
                task["status"] = not task["status"]
                save_database(tasks)
                print("Task statusni muvaffaqiyatli o'zgartirildi!")
                return tasks

        
    
    