

class TelaDoacao:

    def tela_opcoes_consulta(self):
        print('--------------- Consultar doações ---------------')
        print('Escolha o que deseja fazer: ')
        print('1 - Ver todo o registro de doaçoes')
        print('2 - Voltar')
        opcao = input('Escolha uma opção: ')

        while opcao not in ['1','2']:
            print('--------------- Consultar doações ---------------')
            print('Escolha inválida!')
            print('--------------- Consultar doações ---------------')
            print('Escolha o que deseja fazer: ')
            print('1 - Ver todo o registro de doaçoes')
            print('2 - Voltar')

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
        
        try:
            return int(cpf)

        except Exception:
            return 1

    def cpf_nao_cadastrado(self):
        print('Doador não cadastrado! Para realizar a doação é necessário primeiro cadastrar o doador.')
        print('Deseja cadastrar um doador?')
        print('1 - SIM')
        print('2 - NÃO')
        opcao = input('Informe o número da opção escolhida: ')

        while opcao not in ['1', '2']:
            print('Opção inválida! Informe apenas o número da opção escolhida.')
            print('Deseja cadastrar um doador?')
            print('1 - SIM')
            print('2 - NÃO')
            opcao = input('Informe o número da opcao escolhida: ')
        return int(opcao)

    def gato_ou_cachorro(self):
        print('---------------- Doação ---------------')
        print('Bem vindo ao sistema de doação, vamos primeiro realizar o cadastro do seu bichinho')
        print('O animal que será doado é:')
        print('1 - Gato')
        print('2 - Cachorro')
        print('3 - Voltar')
        opcao = input('Informe a opção escolhida: ')

        while opcao not in ['1','2','3']:
            print('---------------- Doação ---------------')
            print('Opção inválida! Digite o número da opção novamente: ')
            print('O animal que será doado é:')
            print('1 - Gato')
            print('2 - Cachorro')
            print('3 - Voltar')
            opcao = input('Informe a opção escolhida: ')

        return int(opcao)    
    
    def finalizar_doacao(self):
        print('---------------- Doação ---------------')
        data = input('Informe a data da doação (dd/mm/aa): ')
        while len(data) != 8:
            print('--------------- Aviso -----------------')
            data = input('Data inválida! Informe a data da doação (dd/mm/aa): ')
            print('--------------- Aviso -----------------')
        motivo = input('Informe o motivo da doação: ')
        print('---------------- Doação ---------------')
        return [data, motivo]

    def sucesso_doacao(self, animal):
        print('--------------- Aviso ----------------')
        print(f'{animal.nome} doado com sucesso!')
        print('--------------- Aviso ----------------')

    def sem_registro_doacoes(self):
        print('--------------- Aviso ----------------')
        print('Ainda não existe nenhuma doação registrada!')
        print('--------------- Aviso ----------------')