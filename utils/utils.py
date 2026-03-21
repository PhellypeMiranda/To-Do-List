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

def write_item():
    while True:
        name = input("Enter new item's name: ").strip().capitalize()
        if name:
            return name
        input("Can't be empty, try again!")

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