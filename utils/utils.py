import os
from models.todo_list import ToDoList
from models.tasks import Task
from storage.storage import Storage

def load_list():
    loader = Storage()
    dict_list = loader.load()
    converted_list = convert_dic_to_obj(dict_list)
    return converted_list

def convert_dic_to_obj(dict_list):
    obj_list = ToDoList()
    for i in dict_list:
        new_task = Task(i["name"], i["checked"])
        obj_list.add_item(new_task)
    return obj_list

def convert_obj_to_json(items_list):
    converted_list = []
    for i in items_list:
        converted_list.append({
            "name": i.name,
            "checked": i.checked,
        })
    return converted_list

def write_item():
    while True:
        name = input("Enter new item's name: ").strip().capitalize()
        if name:
            return name
        input("Can't be empty, try again!")

def check_if_not_empty(items_list):
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
    while True:
        answer = input(f"Are you sure you want to {action}? (Y/N): ").lower().strip()
        if answer == "y":
            return True
        if answer == "n":
            return False
        print("Invalid input, try again.")