class TelaOng():

    def tela_opcoes(self):
        print("-------- Bem vindo a Ong! ---------")
        print("O que deseja hoje?")
        print("1 - Consultar doações")
        print("2 - Consultar adoções")
        print("3 - Doar")
        print("4 - Adotar")
        print("5 - Sair")
        opcao = int(input("Escolha a opcão:")) # se digitar string da erro, tratar

        while opcao not in [1, 2, 3, 4, 5]:
            print('Número inválido, por favor escolha uma das opções abaixo:')  
            print("-------- Bem vindo a Ong! ---------")
            print("O que deseja hoje?")
            print("1 - Consultar doações")
            print("2 - Consultar adoções")
            print("3 - Doar")
            print("4 - Adotar")
            print("5 - Sair")
            opcao = int(input("Escolha a opcão:"))
        return opcao

