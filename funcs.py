import sys
import os
import storage
import json

def ler_json():
    with open("tasks.json", "r") as file:
        return json.load(file)

def mostrar_lista(lista):
    os.system("clear")  # Linux
    print("\nTO DO:")
    if len(lista) == 0:
        print("Lista vazia!\n ")
    else:
        for i, novo in enumerate(lista, start=1):
            print(f"{i} - {novo}")

def adicionar(lista):
    novo = input("Adicione uma tarefa: ")
    lista.append(novo)
    storage.modificar_json(lista)
    input("Tarefa adicionada com sucesso! Aperte qualquer tecla para continuar.")

def remover(lista):
    if len(lista) == 0:
        input("A lista já está vazia!\n ")
    else:
        try:
            removedor = int(input("Qual você deseja remover? "))
            if removedor > len(lista) or removedor <= 0:
                input("Valor inválido! Aperte qualquer tecla para continuar.")
            else:
                confirmacao = input(f"Tem certeza que deseja remover? (Y/N): ").strip()
                if confirmacao.lower() == "y":
                    lista.pop(removedor - 1)
                    storage.modificar_json(lista)
                    input("Tarefa removida com sucesso! Aperte qualquer tecla para continuar.")
        except (ValueError, IndexError):
            input("Valor inválido! Aperte qualquer tecla para continuar.")

def limpar(lista):
    confirmacao = input("Tem certeza que quer limpar a lista? (Y/N) ").strip()
    if confirmacao.lower() == "y":
        lista.clear()
        storage.modificar_json(lista)
        input("Lista esvaziada com sucesso! Aperte qualquer tecla para continuar")

def sair(lista):
    confirmacao = input("Tem certeza que quer sair? (Y/N) ").strip()
    if confirmacao.lower() == "y":
        sys.exit(0)