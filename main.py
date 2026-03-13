from unittest import case


def main():
    #Variável que vai guardar a lista de coisas para fazer
    lista = []

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

            match escolha:
                case 1:
                    if len(lista) == 0:
                        input("Lista vazia!\n ")
                    else:
                        print(f"\nTO DO!")
                        for i in lista:
                            print(f"- {i}")
                        input("Aperte qualquer tecla para continuar")

                case 2:
                    novo = input("Tarefa: ")
                    lista.append(novo)
                    input("Tarefa adicionada com sucesso!\n")

        #Except para caso o usuário digitar uma letra
        except ValueError:
            input("\nValor inválido, por favor digite novamente!\n ")
        #Except para erros não previstos
        except:
            input("\nAlgo deu errado, por favor tente novamente!\n ")



main()