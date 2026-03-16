import json

def read_json():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        with open("tasks.json", "w") as file:
            json.dump([], file)
        return []

def modify_json(items_list):
    with open("tasks.json", "w") as file:
        json.dump(items_list, file, indent=4)