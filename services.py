from todo_list import ToDoList
from tasks import Task
from storage import Storage
from os import exit

def validate_tasks(items_list):
    if not items_list:
        input("The list is empty, press enter to continue...")
        return False
    else:
        try:
            item = int(input("Enter the number of the item: "))
        except ValueError:
            input("invalid input, try again!")
            return False
        if item <= 0 or item > len(items_list):
            input("Invalid input, press enter to continue...")
            return False
        else:
            return item


def show_list(items_list):
    print("\nTO DO:")
    if not items_list:
        print("The list is empty!")
    else:
        count = 1
        for item in items_list:
            if item.checked == True:
                print(f"{count} - [X] {item}")
            else:
                print(f"{count} - [ ] {item}")
            count += 1

def add_item(items_list):
    name = input("Enter item name: ").strip().capitalize()
    if not name:
        input("Invalid input, try again!")
    else:
        new_item = Task(name)
        items_list.add_item(new_item)
        input("Item added, press enter to continue...")

def remove_item(items_list):
    item = validate_tasks(items_list)
    if item != False:
        confirmation = input(f"Are you sure you want to remove {items_list[item - 1]}? (Y/N): ").lower().strip()
        if confirmation == "y":
            items_list.remove_item(item - 1)
            input("Item removed, press enter to continue...")
        else:
            input("Item not removed, press enter to continue...")

def modify_item(items_list):
    item = validate_tasks(items_list)
    if item != False:
        confirmation = input(f"Are you sure you want to modify {items_list[item - 1]}? (Y/N): ").lower().strip()
        if confirmation == "y":
            change = input("Write the new task: ")
            items_list.change_item(item - 1, change)
            input("Item changed, press enter to continue...")
        else:
            input("Item not changed, press enter to continue...")

def mark_item(items_list):
    item = validate_tasks(items_list)
    if item != False:
        confirmation = input(f"Are you sure you want to check/uncheck {items_list[item - 1]}? (Y/N): ").lower().strip()
        if confirmation == "y":
            items_list[item - 1].toggle()
            input("Item marked/unmarked, press enter to continue...")
        else:
            input("Item not marked/unmarked, press enter to continue...")

def clear_list(items_list):
    if not items_list:
        input("The list is empty, press enter to continue...")
        return False
    else:
        confirmation = input(f"Are you sure you want to clear the list? (Y/N): ").lower().strip()
        if confirmation == "y":
            items_list.clear()
            input("List cleared, press enter to continue...")
        else:
            input("List not cleared, press enter to continue...")

def save_exit(items_list):
    Storage.save(items_list)