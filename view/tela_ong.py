class TelaOng():

    def tela_opcoes(self):
        print("-------- Bem vindo a Ong! ---------")
        print("O que deseja hoje?")
        print("1 - Consultar doações")
        print("2 - Consultar adoções")
        print("3 - Doar")
        print("4 - Adotar")
        opcao = int(input("Escolha a opcão:"))

        while opcao not in [1,2,3,4]:
            print('Número inválido, por favor escolha uma das opções abaixo:')  
            print("-------- Bem vindo a Ong! ---------")
            print("O que deseja hoje?")
            print("1 - Consultar doações")
            print("2 - Consultar adoções")
            print("3 - Doar")
            print("4 - Adotar")
            opcao = int(input("Escolha a opcão:"))
        return opcao
