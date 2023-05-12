

class TelaDoador:

    def mostra_tela_cadastro(self):
        print('--------------- Cadastrar Doador ---------------')
        print('Informe seus dados para realizar o cadastro!: ')

        try:
            cpf = int(input('Digite o CPF do Doador ou 1 para cancelar: '))
            if cpf == 1:
                return 1    
        except Exception:
            print('--------------- CPF inválido! revise seus dados e tente novamente. ---------------')
            return 1

        try:
            nome = input('Digite o NOME do Doador ou 1 para cancelar: ')
            if nome == '1':
                return 1
        except Exception:
            print('--------------- NOME inválido! revise seus dados e tente novamente. ---------------')
            return 1            

        try:
            data_nascimento = input('Digite a DATA DE NASCIMENTO do Doador (dd/mm/aa) ou 1 para cancelar: ')
            if data_nascimento == '1':
                return 1
            if len(data_nascimento) < 8:
                raise Exception
        except Exception:
            print('--------------- DATA inválida! revise seus dados e tente novamente. ---------------')
            return 1    

        try:
            endereco = input('Digite o ENDEREÇO do Doador ou 1 para cancelar: ')
            if endereco == '1':
                return 1
        except Exception:
            print('--------------- ENDEREÇO inválido! revise seus dados e tente novamente. ---------------')
            return 1    
        
        lista_cadastro = [cpf, nome, data_nascimento, endereco]    

        return lista_cadastro


    def mostra_sucesso_cadastro(self, cpf):
        print(f'Doador com CPF: {cpf} cadastrado com sucesso!')