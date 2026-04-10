from dominio.entities.tasks import Task
from dominio.entities.todo_list import ToDoList

def convert_from_json(json_file):
    obj_list = ToDoList()
    for i in json_file:
        new_task = Task(i["name"], i["checked"])
        obj_list.add_item(new_task)
    return obj_list

def convert_to_json(tasks_list):
    converted_list = []
    for i in tasks_list:
        converted_list.append({
            "name": i.name,
            "checked": i.checked,
        })
    return converted_list