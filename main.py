def main():
#Menu principal, o usuário vai escolher qual caminho seguir.
    while True:
        try:
            escolha = int(input("O que gostaria de fazer?\n"
                            "1 - Ver lista\n"
                            "2 - Adicionar item a lista\n"
                            "3 - Remover item da lista\n"
                            "4 - Apagar lista\n"
                            "5 - Sair\n"
                            "Digite um valor: "))
            break
        except ValueError:
            input("\nValor inválido, por favor digite novamente!\n ")

        except:
            input("\nAlgo deu errado, por favor tente novamente!\n ")

main()