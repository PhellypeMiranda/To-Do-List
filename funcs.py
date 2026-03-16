import sys
import os
import storage

def mostrar_lista():
    lista = storage.ler_json()
    limpar_tela()  # Linux
    print("\nTO DO:")
    if len(lista) == 0:
        print("Lista vazia!\n ")
    else:
        for i, novo in enumerate(lista, start=1):
            print(f"{i} - {novo}")

def adicionar():
    lista = storage.ler_json()
    novo = input("Adicione uma tarefa: ")
    lista.append(novo)
    storage.modificar_json(lista)
    input("Tarefa adicionada com sucesso! Aperte qualquer tecla para continuar.")

def remover():
    lista = storage.ler_json()
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

def limpar_lista():
    lista = storage.ler_json()
    confirmacao = input("Tem certeza que quer limpar a lista? (Y/N) ").strip()
    if confirmacao.lower() == "y":
        lista.clear()
        storage.modificar_json(lista)
        input("Lista esvaziada com sucesso! Aperte qualquer tecla para continuar")

def sair():
    confirmacao = input("Tem certeza que quer sair? (Y/N) ").strip()
    if confirmacao.lower() == "y":
        sys.exit(0)

def limpar_tela():
    if os.name == "nt":  # Windows
        os.system("cls")
    else:  # Linux / macOS
        os.system("clear")