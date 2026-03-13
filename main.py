import funcs

def escolhas(escolha, lista):
    match escolha:
        case 1:
            funcs.adicionar(lista)
        case 2:
            funcs.remover(lista)
        case 3:
            funcs.limpar(lista)
        case 4:
            funcs.sair(lista)
        case _:
            input("Opção inválida!")

def main():
    lista = funcs.ler_json()
    #Menu principal, o usuário vai escolher qual caminho seguir.
    while True:
        try:
            funcs.mostrar_lista(lista)
            escolha = int(input("\nO que gostaria de fazer?\n"
                            "1 - Adicionar item a lista\n"
                            "2 - Remover item da lista\n"
                            "3 - Apagar lista\n"
                            "4 - Sair\n"
                            "Digite um valor: "))

            escolhas(escolha, lista)

        #Except para caso o usuário digitar uma letra
        except (ValueError, IndexError):
            input("\nValor inválido, por favor digite novamente!\n ")
        #Except para erros não previstos

main()