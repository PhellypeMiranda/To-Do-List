import sys
from models.tasks import Task
from storage.storage import Storage
import utils.utils as utils
from interface.ui import TodoUI

class Services:
    def __init__(self):
        self.items_list = None

    def load_on_menu(self):
        self.items_list = utils.load_list()

    def add_item(self,name):
        new_item = Task(name)
        self.items_list.add_item(new_item)
        self.save()

    def remove_item(self, index):
        self.items_list.remove_item(index)
        self.save()

    def modify_item(self, index, name):
        self.items_list.change_item(index, name)
        self.save()

    def mark_item(self,index):
        self.items_list[index].toggle()
        self.save()

    def clear_list(self):
        self.items_list.clear()
        self.save()

    def save(self):
            converted_list = utils.convert_obj_to_json(self.items_list)
            storage = Storage()
            storage.save(converted_list)

    @staticmethod
    def exit_program():
            sys.exit()