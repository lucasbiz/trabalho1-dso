from PySimpleGUI import PySimpleGUI as sg

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

    def pegar_gato_pelo_numero(self):

        sg.theme('SandyBeach')
        layout = [[sg.Text(f'Informe o número do chip do gato desejado: '), sg.InputText(key='numero_chip', size=(15,1))]]
        layout.append([sg.Button('Confirmar', size=(20, 1)), sg.Button('Voltar', size=(20, 1))])

        
        self.__window = sg.Window('Ong das Patinhas').Layout(layout)

        numero_correto = False

        while numero_correto == False:

            button, values = self.__window.Read()
            if button == 'Confirmar':
                # VALIDACAO NUMERO CHIP
                try:
                    numero = int(values['numero_chip'])
                    numero_correto = True
                    sg.popup('Gato encontrado! Prosseguindo adoção...')
                    self.__window.close()
                    return numero

                except Exception:
                    sg.popup('NUMERO DO CHIP INVÁLIDO')
                    self.__window['numero_chip'].Update('')
                    return 1
                

            if button == 'Voltar':
                numero_correto = True
                self.__window.close()
                return 1


    def gato_nao_encontrado(self):
        sg.popup('GATO NÃO ENCONTRADO')
