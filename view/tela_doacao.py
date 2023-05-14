

class TelaDoacao:

    def tela_opcoes_consulta(self):
        print('--------------- Consultar doações ---------------')
        print('Escolha o que deseja fazer: ')
        print('1 - Ver todo o registro de doaçoes')
        print('2 - Consultar doações por um período')
        print('3 - Voltar')
        opcao = input('Escolha uma opção: ')

        while opcao not in ['1','2','3']:
            print('--------------- Consultar doações ---------------')
            print('Escolha inválida!')
            print('--------------- Consultar doações ---------------')
            print('Escolha o que deseja fazer: ')
            print('1 - Ver todo o registro de doaçoes')
            print('2 - Consultar doações por um período')
            print('3 - Voltar')

            opcao = input('Escolha uma opção: ')   
         
        return int(opcao)

    def tela_opcoes_doacao(self):
        print('--------------- Doações ---------------')
        print('Escolha o que deseja fazer: ')
        print('1 - Doar um animal')
        print('2 - Cadastrar um doador')
        print('3 - Voltar')
        opcao = input('Escolha uma opção: ')

        while opcao not in ['1','2','3']:
            print('--------------- Doações ---------------')
            print('Escolha inválida!')
            print('--------------- Doações ---------------')
            print('Escolha o que deseja fazer: ')
            print('1 - Doar um animal')
            print('2 - Cadastrar um doador')
            print('3 - Voltar')

            opcao = input('Escolha uma opção: ')   
         
        return int(opcao)

    def mostra_doacoes(self,doacao):
        print(doacao)

    def pedir_cpf(self):
        cpf = input('Informe o CPF do doador: ')
        return cpf

    def cpf_nao_cadastrado(self):
        print('Doador não cadastrado! Para realizar a doação é necessário primeiro cadastrar o doador.')

