import json

class Storage:
    def __init__(self, file="tasks.json"):
        self.File = file

    def save(self, converted_list):
        with open(self.file, "w") as f:
            json.dump(converted_list, f, indent=4)
            return 0

    def load(self):
        try:
            with open(self.file, "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []