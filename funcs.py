import sys
import os
import storage

def count(items_list):
    check = {
        "finished": 0,
        "unfinished": 0
    }
    for item in items_list:
        if item["checked"] == 1:
            check["finished"] += 1
        else:
            check["unfinished"] += 1
    return check

def get_list():
    return storage.read_json()

def show_list(items_list):
    clear_screen()  # Linux
    print("\nTO DO:")
    if len(items_list) == 0:
        print("Empty list!\n ")
    else:
        for i, item in enumerate(items_list, start=1):
            if item["checked"] == 1:
                print(f"{i} - [X] {item['name']}")
            else:
                print(f"{i} - [ ] {item['name']}")

def add_item(items_list):
    while True:
        new_task = input("Add a task: ").strip().capitalize()
        if not new_task:
            print("Please type something.")
            continue
        else:
            items_list.append({"name": new_task, "checked": 0})
            input("Task added successfully. Press Enter to continue...")
            break


def mark_as_checked(items_list):
    if not items_list:
        input("The list is empty!\n ")
    else:
        while True:
            try:
                item = int(input("Which one do you want to mark/unmark? "))
                if item > len(items_list) or item <= 0:
                    print("Invalid value! try again.")
                    continue
                else:
                    changed_item = items_list[item - 1]
                    if changed_item["checked"] == 0:
                        changed_item["checked"] = 1
                        break
                    else:
                        changed_item["checked"] = 0
                        break
            except (ValueError, IndexError):
                print("Invalid value! try again.")
                continue

def change_item(items_list):
    if not items_list:
        input("The list is empty!\n ")
    else:
        while True:
            try:
                item = int(input("Which one do you want change? "))
                if item > len(items_list) or item <= 0:
                    print("Invalid value! try again.")
                    continue
                else:
                    while True:
                        change = input("Type the new task: ").strip()
                        if not change:
                            print("Type the name of the task")
                            continue
                        else:
                            changed_item = items_list[item - 1]
                            changed_item["name"] = change
                            break
                    break
            except (ValueError, IndexError):
                print("Invalid value! try again.")
                continue

def remove_item(items_list):
    if not items_list:
        input("The list is empty!\n ")
    else:
        while True:
            try:
                item = int(input("Which one do you want to remove? "))
                if item > len(items_list) or item <= 0:
                    print("Invalid value! try again.")
                    continue
                else:
                    changed_item = items_list[item - 1]
                    confirmation = input(f"Are you sure you want to remove {changed_item["name"]}? (Y/N): ").strip()
                    if confirmation.lower() == "y":
                        items_list.pop(item - 1)
                        break
                    else:
                        break
            except (ValueError, IndexError):
                print("Invalid value! try again.")
                continue

def clear_list(items_list):
    confirmation = input("Are you sure you want to clear the list? (Y/N) ").strip()
    if confirmation.lower() == "y":
        items_list.clear()
        input("The list cleared successfully.")

def save_and_exit(items_list):
    confirmation = input("Are you sure you want save and exit? (Y/N) ").strip()
    if confirmation.lower() == "y" and confirmation.lower() != "n":
        storage.modify_json(items_list)
        sys.exit(0)

def clear_screen():
    if os.name == "nt":  # Windows
        os.system("cls")
    else:  # Linux / macOS
        os.system("clear")