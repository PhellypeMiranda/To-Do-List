import json

def modificar_json(lista):
    conversor = json.dumps(lista)
    with open("tasks.json", "w") as file:
        file.write(conversor)