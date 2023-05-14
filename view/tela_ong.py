class TelaOng():

    def tela_opcoes(self):
        print("-------- Bem vindo a Ong! ---------")
        print("O que deseja hoje?")
        print("1 - Consultar doações")
        print("2 - Consultar adoções")
        print("3 - Consultar doadores")
        print("4 - Consultar adotantes")
        print("5 - Doar")
        print("6 - Adotar")
        print("7 - Sair")
        opcao = input("Escolha a opcão:")

        while opcao not in ['1','2','3','4','5','6','7']:
            print('---------------------------------------------------------')
            print('Número inválido, por favor escolha uma das opções abaixo:')  
            print('---------------------------------------------------------')
            print("-------- Bem vindo a Ong! ---------")
            print("O que deseja hoje?")
            print("1 - Consultar doações")
            print("2 - Consultar adoções")
            print("3 - Consultar doadores")
            print("4 - Consultar adotantes")
            print("5 - Doar")
            print("6 - Adotar")
            print("7 - Sair")
            opcao = input("Escolha a opcão:")
        return int(opcao)


