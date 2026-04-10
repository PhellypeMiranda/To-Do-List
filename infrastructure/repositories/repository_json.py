import json
from infrastructure.config.config import DATA_DIR
from infrastructure.mappers.todo_mapper import *

class RepositoryJson:
    def __init__(self, file="tasks.json"):
        self.file = DATA_DIR / file
        self.file.parent.mkdir(parents=True, exist_ok=True)

    def save(self, tasks_list):
        converted_list = convert_to_json(tasks_list)
        with open(self.file, "w") as f:
            json.dump(converted_list, f, indent=4)
            return 0

    def load(self):
        try:
            with open(self.file, "r") as f:
                data_json = json.load(f)
                converted_data = convert_from_json(data_json)
                return converted_data
        except (FileNotFoundError, json.JSONDecodeError):
            return []