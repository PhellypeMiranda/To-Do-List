import os
from todo_list import ToDoList
from tasks import Task

def check_if_empty_list(items_list):
    if not items_list:
        input("The list is empty, press enter to continue...")
        return False
    else:
        return True

def create_value(items_list):
    try:
        item = int(input("Enter the number of the item: "))
        if item <= 0 or item > len(items_list):
            input("Invalid input, press enter to continue...")
            return False
        else:
            return item
    except ValueError:
        input("invalid input, try again!")
        return False

def clear_screen():
    if os.name == "nt":  # Windows
        os.system("cls")
    else:  # Linux / macOS
        os.system("clear")

def confirmation(action):
    confirmation = input(f"Are you sure you want to {action}? (Y/N): ").lower().strip()
    if confirmation == "y":
        return True

def convert_obj_to_json(items_list):
    converted_list = []
    for i in items_list:
        converted_list.append({
            "name": i.name,
            "checked": i.checked,
        })
    return converted_list

def convert_dic_to_obj(items_list):
    converted_list = ToDoList()
    for i in items_list:
        new_task = Task(i["name"], i["checked"])
        converted_list.add_item(new_task)
    return converted_list