import json

def ler_json():
    with open("tasks.json", "r") as file:
        return json.load(file)

def modificar_json(lista):
    conversor = json.dumps(lista)
    with open("tasks.json", "w") as file:
        file.write(conversor)