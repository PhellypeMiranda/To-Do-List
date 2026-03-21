import sys
from models.tasks import Task
from storage.storage import Storage
import utils.utils as utils


def load_list():
    loader = Storage()
    items_list = loader.load()
    converted_list = utils.convert_dic_to_obj(items_list)
    return converted_list


def show_list(items_list):
    utils.clear_screen()
    print("\nTO DO:")
    if not items_list:
        print("The list is empty!")
    else:
        count = 1
        for item in items_list:
            if item.checked:
                print(f"{count} - [X] {item}")
            else:
                print(f"{count} - [ ] {item}")
            count += 1


def write_item():
    while True:
        name = input("Enter new item's name: ").strip().capitalize()
        if name:
            return name
        input("Can't be empty, try again!")


def add_item(items_list):
    name = write_item()
    if name:
        new_item = Task(name)
        items_list.add_item(new_item)
        input("Item added, press enter to continue...")


def remove_item(items_list):
    if utils.check_if_not_empty(items_list):
        item = utils.create_value(items_list)
        if item != False:
            if utils.confirmation('remove item'):
                items_list.remove_item(item - 1)
                input("Item removed, press enter to continue...")
            else:
                input("Item not removed, press enter to continue...")


def modify_item(items_list):
    if utils.check_if_not_empty(items_list):
        item = utils.create_value(items_list)
        if item != False:
            new_item = write_item()
            if utils.confirmation('modify item'):
                items_list.change_item(item - 1, new_item)
                input("Item changed, press enter to continue...")


def mark_item(items_list):
    if utils.check_if_not_empty(items_list):
        item = utils.create_value(items_list)
        if item != False:
            if utils.confirmation('mark item'):
                items_list[item - 1].toggle()
                input("Item marked/unmarked, press enter to continue...")


def clear_list(items_list):
    if utils.check_if_not_empty(items_list):
        if utils.confirmation('clear the list'):
            items_list.clear()
            input("List cleared, press enter to continue...")
        else:
            input("List not cleared, press enter to continue...")


def save(items_list):
    if utils.confirmation('save'):
        conv = utils.convert_obj_to_json(items_list)
        storage = Storage()
        storage.save(conv)
        input("List saved, press enter to continue...")


def exit(items_list):
    if utils.confirmation('save and exit'):
        conv = utils.convert_obj_to_json(items_list)
        storage = Storage()
        storage.save(conv)
        sys.exit()
