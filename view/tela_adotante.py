class TelaAdotante:

    def mostra_tela_cadastro(self):
        print('--------------- Cadastrar adotante ---------------')
        print('Informe seus dados para realizar o cadastro!: ')

        try:
            cpf = int(input('Digite o CPF do adotante ou 1 para cancelar: '))
            if cpf == 1:
                return 1    
        except Exception:
            print('--------------- CPF inválido! revise seus dados e tente novamente. ---------------')
            return 1
        try:
            nome = input('Digite o NOME do adotante ou 1 para cancelar: ')
            if nome == '1':
                return 1
        except Exception:
            print('--------------- NOME inválido! revise seus dados e tente novamente. ---------------')
            return 1    

        try:
            data_nascimento = input('Digite a DATA DE NASCIMENTO do adotante (dd/mm/aa) ou 1 para cancelar: ')
            if data_nascimento == '1':
                return 1
            if len(data_nascimento) != 8:
                raise Exception
        except Exception:
            print('--------------- DATA inválida! revise seus dados e tente novamente. ---------------')
            return 1    

        try:
            endereco = input('Digite o ENDEREÇO do adotante ou 1 para cancelar: ')
            if endereco == '1':
                return 1
        except Exception:
            print('--------------- ENDEREÇO inválido! revise seus dados e tente novamente. ---------------')
            return 1    

        try:
            tipo_habitacao = input('Digite o TIPO DE HABITACAO do adotante (1 - Pequena/ 2 - Media /3 - Grande ) ou 1 para cancelar: ')
            if tipo_habitacao == '1':
                return 1
        except Exception:
            print('--------------- TIPO DE HABITACAO inválida! revise seus dados e tente novamente. ---------------')
            return 1   
        
        lista_cadastro = [cpf, nome, data_nascimento, endereco, tipo_habitacao]    

        return lista_cadastro


    def mostra_sucesso_cadastro(self, cpf):
        print(f'Adotante com CPF: {cpf} cadastrado com sucesso!')

    def mostra_adotantees(self, adotante):
        print(adotante)

    def sem_adotantees(self):
        print('Não existem adotantes cadastrados!')

    def cpf_ja_cadastrado(self, cpf):
        print('--------------- Aviso ---------------')
        print(f'CPF {cpf} já cadastrado como adotante!')
        print('--------------- Aviso ---------------')
    
    def cpf_nao_encontrado(self, cpf):
        print('--------------- Aviso ---------------')
        print(f'CPF {cpf} não encontrado!')
        print('--------------- Aviso ---------------')
