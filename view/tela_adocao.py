class TelaAdocao:

    def tela_opcoes_consulta(self):
        print('--------------- Consultar adoções ---------------')
        print('Escolha o que deseja fazer: ')
        print('1 - Ver todo o registro de adoções')
        print('2 - Consultar adoções por um período')
        print('3 - Voltar')
        opcao = input('Escolha uma opção: ')

        while opcao not in ['1','2','3']:
            print('--------------- Consultar adoções ---------------')
            print('Escolha inválida!')
            print('--------------- Consultar adoções ---------------')
            print('Escolha o que deseja fazer: ')
            print('1 - Ver todo o registro de adoções')
            print('2 - Consultar adoções por um período')
            print('3 - Voltar')

            opcao = input('Escolha uma opção: ')   
         
        return int(opcao)

    def tela_opcoes_adocao(self):
        print('--------------- Adoções ---------------')
        print('Escolha o que deseja fazer: ')
        print('1 - Adotar um animal')
        print('2 - Cadastrar um Adotante')
        print('3 - Voltar')
        opcao = input('Escolha uma opção: ')

        while opcao not in ['1','2','3']:
            print('--------------- adoções ---------------')
            print('Escolha inválida!')
            print('--------------- adoções ---------------')
            print('Escolha o que deseja fazer: ')
            print('1 - Adotar um animal')
            print('2 - Cadastrar um Adotante')
            print('3 - Voltar')

            opcao = input('Escolha uma opção: ')   
         
        return int(opcao)

    def mostra_doacoes(self,adocao):
        print(adocao)

    def pedir_cpf(self):
        cpf = input('Informe o CPF do Adotante: ')
        
        try:
            return int(cpf)

        except Exception:
            return 1

    def cpf_nao_cadastrado(self):
        print('Adotante não cadastrado! Para realizar a adoção é necessário primeiro cadastrar o Adotante.')
        print('Deseja cadastrar um Adotante?')
        print('1 - SIM')
        print('2 - NÃO')
        opcao = input('Informe o número da opção escolhida: ')

        while opcao not in ['1', '2']:
            print('Opção inválida! Informe apenas o número da opção escolhida.')
            print('Deseja cadastrar um Adotante?')
            print('1 - SIM')
            print('2 - NÃO')
            opcao = input('Informe o número da opcao escolhida: ')
        return int(opcao)

    def gato_ou_cachorro(self):
        print('---------------- Adoção ---------------')
        print('Bem vindo ao sistema de adoção, vamos primeiro realizar o cadastro do seu bichinho')
        print('O animal que será adotado é:')
        print('1 - Gato')
        print('2 - Cachorro')
        print('3 - Voltar')
        opcao = input('Informe a opção escolhida: ')

        while opcao not in ['1','2','3']:
            print('---------------- Adoção ---------------')
            print('Opção inválida! Digite o número da opção novamente: ')
            print('O animal que será adotado é:')
            print('1 - Gato')
            print('2 - Cachorro')
            print('3 - Voltar')
            opcao = input('Informe a opção escolhida: ')

        return int(opcao)    
    
    def finalizar_adocao(self):
        print('---------------- Adoção ---------------')
        data = input('Informe a data da adoção (dd/mm/aa): ')
        while len(data) != 8:
            print('--------------- Aviso -----------------')
            data = input('Data inválida! Informe a data da adoção (dd/mm/aa): ')
            print('--------------- Aviso -----------------')
        print('Assinar termo de responsabilidade: ')
        print('1 - Assinar')
        print('2 - Não assinar')
        assinar_termo = input('Escolha uma opção ')
        while assinar_termo not in ['1','2']:
            print('Opção inválida!')
            print('Assinar termo de responsabilidade: ')
            print('1 - Assinar')
            print('2 - Não assinar')
            assinar_termo = input('Escolha uma opção ')

        print('---------------- Adoção ---------------')
        return [data, int(assinar_termo)]

    def sucesso_adocao(self, animal):
        print('--------------- Aviso ----------------')
        print(f'{animal} adotado com sucesso!')
        print('--------------- Aviso ----------------')
    
    def adocao_cancelada_termo():
        print('Não é possivel adotar um animal sem assinar o termo, adoção cancelada!')