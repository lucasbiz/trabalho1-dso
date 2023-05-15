

class TelaCachorro:

    def cachorro_ja_cadastrado(self, numero_chip):
        print('--------------- Aviso -----------------')
        print(f'O cachorro com número do chip {numero_chip} já está cadastrado!')
        print('--------------- Aviso -----------------')

    def mostra_tela_cadastro(self):
        print('--------------- Cadastrar Cachorro ---------------')
        print('Informe seus dados para realizar o cadastro!: ')

        try:
            numero_chip = int(input('Digite o NÚMERO DO CHIP do Cachorro ou 1 para cancelar: '))
            if numero_chip == 1:
                return 1    
        except Exception:
            print('--------------- Número inválido! revise os dados e tente novamente. ---------------')
            return 1
        try:
            nome = input('Digite o NOME do cachorro ou 1 para cancelar: ')
            if nome == '1':
                return 1
        except Exception:
            print('--------------- NOME inválido! revise seus dados e tente novamente. ---------------')
            return 1    

        try:
            raca = input('Digite a RAÇA do Cachorro ou 1 para cancelar: ')
            if raca == '1':
                return 1
        except Exception:
            print('--------------- RAÇA inválida! revise seus dados e tente novamente. ---------------')
            return 1    

        try:
            tamanho = input('Digite o TAMANHO do Cachorro (1 - pequeno/ 2 - medio/ 3 - grande) ou 4 para cancelar: ')
            if tamanho == '4':
                return 1
        except Exception:
            print('--------------- TAMANHO inválido! revise seus dados e tente novamente. ---------------')
            return 1    
        
        lista_cadastro = [numero_chip, nome, raca, tamanho]    

        return lista_cadastro
    
    def sucesso_cadastro_cachorro(self):
        print('--------------- Aviso ----------------')
        print('Cachorro cadastrado com sucesso!')
        print('--------------- Aviso ----------------')
    
