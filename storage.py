import json

class Storage:
    def __init__(self, file="tasks.json"):
        self.File = file

    def save(self, items_list):
        with open(self.File, "w") as f:
            json.dump(items_list, f, indent=4)