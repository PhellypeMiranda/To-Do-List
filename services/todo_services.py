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
        if utils.check_if_not_empty(self.items_list):
            item = utils.create_value(self.items_list)
            if item:
                if utils.confirmation('remove item'):
                    self.items_list.remove_item(item - 1)
                    input("Item removed, press enter to continue...")
                else:
                    input("Item not removed, press enter to continue...")


    def modify_item(self):
        if utils.check_if_not_empty(self.items_list):
            item = utils.create_value(self.items_list)
            if item:
                new_item = utils.write_item()
                if utils.confirmation('modify item'):
                    self.items_list.change_item(item - 1, new_item)
                    input("Item changed, press enter to continue...")


    def mark_item(self):
        if utils.check_if_not_empty(self.items_list):
            item = utils.create_value(self.items_list)
            if item:
                if utils.confirmation('mark item'):
                    self.items_list[item - 1].toggle()
                    input("Item marked/unmarked, press enter to continue...")


    def clear_list(self):
        if utils.check_if_not_empty(self.items_list):
            if utils.confirmation('clear the list'):
                self.items_list.clear()
                input("List cleared, press enter to continue...")
            else:
                input("List not cleared, press enter to continue...")


    def save(self):
        if utils.confirmation('save'):
            conv = utils.convert_obj_to_json(self.items_list)
            storage = Storage()
            storage.save(conv)
            input("List saved, press enter to continue...")


    def exit(self):
        if utils.confirmation('save and exit'):
            conv = utils.convert_obj_to_json(self.items_list)
            storage = Storage()
            storage.save(conv)
            sys.exit()
