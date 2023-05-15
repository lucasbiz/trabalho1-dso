

class TelaGato:

    def gato_ja_cadastrado(self, numero_chip):
        print('--------------- Aviso -----------------')
        print(f'O gato com número do chip {numero_chip} já está cadastrado!')
        print('--------------- Aviso -----------------')

    def mostra_tela_cadastro(self):
        print('--------------- Cadastrar gato ---------------')
        print('Informe seus dados para realizar o cadastro!: ')

        try:
            numero_chip = int(input('Digite o NÚMERO DO CHIP do gato ou 1 para cancelar: '))
            if numero_chip == 1:
                return 1    
        except Exception:
            print('--------------- Número inválido! revise os dados e tente novamente. ---------------')
            return 1
        try:
            nome = input('Digite o NOME do gato ou 1 para cancelar: ')
            if nome == '1':
                return 1
        except Exception:
            print('--------------- NOME inválido! revise seus dados e tente novamente. ---------------')
            return 1    

        try:
            raca = input('Digite a RAÇA do gato ou 1 para cancelar: ')
            if raca == '1':
                return 1
        except Exception:
            print('--------------- RAÇA inválida! revise seus dados e tente novamente. ---------------')
            return 1     
        
        lista_cadastro = [numero_chip, nome, raca]    

        return lista_cadastro
    
    def sucesso_cadastro_gato(self):
        print('--------------- Aviso ----------------')
        print('Gato cadastrado com sucesso!')
        print('--------------- Aviso ----------------')

    def sem_gatos(self):
        print('Não existem gatos cadastrados!')

    def mostra_gatos(self, gato):
        print(gato)