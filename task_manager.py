from mongo_crud import MongoCRUD
import os, time

database = MongoCRUD(
    host="localhost",
    port=27017,
    database_name="task_manager",
    collection_name="tasks",
)


def add_task() -> None:
    os.system("cls")
    task_name = input("Enter new task name: ")
    task_description = input("Enter new task description: ")
    document = {"task": task_name, "description": task_description, "status": "pending"}
    database.insert_one_document(document)
    print(f"\nTask {task_name} has been added")
    time.sleep(1.5)


def view_all_tasks() -> None:
    os.system("cls")
    all_tasks = database.find_documents({})
    for task in all_tasks:
        print(
            f"\nTask: {task['task']}\nDescription: {task['description']}\nStatus: {task['status']}"
        )
    input("\nPress enter to continue...")


def main_menu() -> None:
    while True:
        os.system("cls")
        print("\n------------------\n|--TASK MANAGER--|\n------------------")
        category: str = input(
            "--Menu--\n1. Add new task\n2. View all tasks\n3. Update the status of a task\n4. Delete a task\n5. Exit\n\nEnter number of selection: "
        )
        if category.isnumeric() == True:
            if category == "1":
                add_task()
            elif category == "2":
                view_all_tasks()
            elif category == "3":
                pass
            elif category == "4":
                pass
            elif category == "5":
                print("\nBye.")
                break
            else:
                print("\nThere is no such selection")
                time.sleep(1.5)
        else:
            print(
                "\nPlease enter number from list provided without any symbols and spaces."
            )
            time.sleep(2)


main_menu()
