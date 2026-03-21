import sys
from models.tasks import Task
from storage.storage import Storage
import utils.utils as utils

class Services:
    def __init__(self):
        self.items_list = utils.load_list()

    def show_list(self):
        utils.clear_screen()
        print("\nTO DO:")
        if not self.items_list:
            print("The list is empty!")
        else:
            count = 1
            for item in self.items_list:
                if item.checked:
                    print(f"{count} - [X] {item}")
                else:
                    print(f"{count} - [ ] {item}")
                count += 1

    def add_item(self):
        name = utils.write_item()
        if name:
            new_item = Task(name)
            self.items_list.add_item(new_item)
            input("Item added, press enter to continue...")

    def remove_item(self):
        if self.check_if_not_empty():
            item = self.create_value()
            if item:
                if utils.confirmation('remove item'):
                    self.items_list.remove_item(item - 1)
                    input("Item removed, press enter to continue...")
                else:
                    input("Item not removed, press enter to continue...")

    def modify_item(self):
        if self.check_if_not_empty():
            item = self.create_value()
            if item:
                new_item = utils.write_item()
                if utils.confirmation('modify item'):
                    self.items_list.change_item(item - 1, new_item)
                    input("Item changed, press enter to continue...")

    def mark_item(self):
        if self.check_if_not_empty():
            item = self.create_value()
            if item:
                if utils.confirmation('mark item'):
                    self.items_list[item - 1].toggle()
                    input("Item marked/unmarked, press enter to continue...")

    def clear_list(self):
        if self.check_if_not_empty():
            if utils.confirmation('clear the list'):
                self.items_list.clear()
                input("List cleared, press enter to continue...")
            else:
                input("List not cleared, press enter to continue...")

    def save(self):
        if utils.confirmation('save'):
            converted_list = self.convert_obj_to_json()
            storage = Storage()
            storage.save(converted_list)
            input("List saved, press enter to continue...")

    def exit(self):
        if utils.confirmation('save and exit'):
            conv = utils.convert_obj_to_json(self.items_list)
            storage = Storage()
            storage.save(conv)
            sys.exit()

    def check_if_not_empty(self):
        if not self.items_list:
            input("The list is empty, press enter to continue...")
            return False
        else:
            return True

    def create_value(self):
        try:
            item = int(input("Enter the number of the item: "))
            if item <= 0 or item > len(self.items_list):
                input("Invalid input, press enter to continue...")
                return False
            else:
                return item
        except ValueError:
            input("invalid input, try again!")
            return False

    def convert_obj_to_json(self):
        converted_list = []
        for i in self.items_list:
            converted_list.append({
                "name": i.name,
                "checked": i.checked,
            })
        return converted_list