import sys
import os
import storage

def get_list():
    items_list = storage.read_json()
    return items_list

def show_list(items_list):
    clear_screen()  # Linux
    print("\nTO DO:")
    if len(items_list) == 0:
        print("Empty list!\n ")
    else:
        for i, item in enumerate(items_list, start=1):
            print(f"{i} - {item}")

def add_item(items_list):
    new_task = input("Add a task: ")
    items_list.append(new_task)
    storage.modify_json(items_list)
    input("Task added successfully. Press Enter to continue...")

def remove_item(items_list):
    if len(items_list) == 0:
        input("The list is empty!\n ")
    else:
        try:
            remover = int(input("Which one do you want to remove? "))
            if remover > len(items_list) or remover <= 0:
                input("Invalid value! try again.")
            else:
                confirmation = input(f"Are you sure you want to remove {items_list[remover - 1]}? (Y/N): ").strip()
                if confirmation.lower() == "y":
                    items_list.pop(remover - 1)
                    storage.modify_json(items_list)
                    input("Item removed successfully.")
        except (ValueError, IndexError):
            input("Invalid value! try again.")

def clear_list(items_list):
    confirmation = input("Are you sure you want to clear the list? (Y/N) ").strip()
    if confirmation.lower() == "y":
        items_list.clear()
        storage.modify_json(items_list)
        input("The list cleared successfully.")

def save_and_exit():
    confirmation = input("Are you sure you want save and exit? (Y/N) ").strip()
    if confirmation.lower() == "y":
        sys.exit(0)

def clear_screen():
    if os.name == "nt":  # Windows
        os.system("cls")
    else:  # Linux / macOS
        os.system("clear")