from PySimpleGUI import PySimpleGUI as sg

class TelaGato:

    def mostra_tela_cadastro(self):
        self.iniciar_tela()
        informacoes_cadastro = self.validacoes_cadastro()
        return informacoes_cadastro
    
    def validacoes_cadastro(self):

        cadastro_finalizado = False

        while cadastro_finalizado == False:
            button, values = self.__window.Read()
            informacoes_cadastro = []

            if button == 'Confirmar':

                # VALIDACAO CPF
                if len(values['cpf']) != 11:
                    sg.popup('CPF INVÁLIDO')
                    self.__window['cpf'].Update('')
                else:
                    try:
                        informacoes_cadastro.append(int(values['cpf']))
                    except Exception:
                        sg.popup('CPF INVÁLIDO')
                        self.__window['cpf'].Update('')

                # VALIDACAO NOME
                if len(values['nome']) > 50 or len(values['nome']) == 0:
                    sg.popup('NOME INVÁLIDO')
                    self.__window['nome'].Update('')
                else:
                    try:
                        informacoes_cadastro.append(values['nome'])
                    except Exception:
                        sg.popup('NOME INVÁLIDO')
                        self.__window['nome'].Update('')

                # VALIDACAO DATA DE NASCIMENTO
                if len(values['data_nascimento']) != 10:
                    sg.popup('DATA INVÁLIDA')
                    self.__window['data_nascimento'].Update('')
                else:
                    try:
                        informacoes_cadastro.append(values['data_nascimento'])
                    except Exception:
                        sg.popup('DATA INVÁLIDA')
                        self.__window['data_nascimento'].Update('')

                # VALIDACAO ENDEREÇO
                if len(values['endereco']) == 0:
                    sg.popup('ENDEREÇO INVÁLIDO')
                    self.__window['endereco'].Update('')
                else:
                    try:
                        informacoes_cadastro.append(values['endereco'])
                    except Exception:
                        sg.popup('ENDEREÇO INVÁLIDO')
                        self.__window['endereco'].Update('')

            if button == 'Voltar':
                cadastro_finalizado = True
                self.close()
                return 1
        # FIM VALIDAÇÕES, RETORNA LISTA DE INFORMAÇÕES
        self.close()
        return informacoes_cadastro

    def iniciar_tela(self):

        sg.theme('SandyBeach')

        layout = [
            [sg.Text('Cadastro de novo Gato', size=(50, 1))],
            [sg.Text('Informe os dados para prosseguir:')],
            [sg.Text('Número do Chip: ', size=(25, 1)), sg.InputText(key='numero_chip', size=(20, 1))],
            [sg.Text('Nome: ', size=(25, 1)), sg.InputText(key='nome', size=(20, 1))],
            [sg.Text('Raça', size=(25, 1)), sg.InputText(key='raca', size=(20, 1))],
            [sg.Text('Histórico de Vacinação', size=(25, 1)), sg.InputText(key='endereco', size=(20, 1))],
            [sg.Button('Confirmar', size=(20, 1)), sg.Button('Voltar', size=(20, 1))]
        ]

        self.__window = sg.Window('Ong das Patinhas').Layout(layout)

    def mostra_sucesso_cadastro(self, numero_chip):
        sg.popup(f'Gato com número do chip {numero_chip} cadastrado com sucesso!')

    # fecha a tela 
    def close(self):
        self.__window.Close()

    # Tela de cadastro de novo gato


# ==================== FIM CADASTRO ==================== 
   
    # def mostra_tela_cadastro(self):
    #     print('--------------- Cadastrar gato ---------------')
    #     print('Informe seus dados para realizar o cadastro!: ')

    #     try:
    #         numero_chip = int(input('Digite o NÚMERO DO CHIP do gato ou 1 para cancelar: '))
    #         if numero_chip == 1:
    #             return 1    
    #     except Exception:
    #         print('--------------- Número inválido! revise os dados e tente novamente. ---------------')
    #         return 1
    #     try:
    #         nome = input('Digite o NOME do gato ou 1 para cancelar: ')
    #         if nome == '1':
    #             return 1
    #     except Exception:
    #         print('--------------- NOME inválido! revise seus dados e tente novamente. ---------------')
    #         return 1    

    #     try:
    #         raca = input('Digite a RAÇA do gato ou 1 para cancelar: ')
    #         if raca == '1':
    #             return 1
    #     except Exception:
    #         print('--------------- RAÇA inválida! revise seus dados e tente novamente. ---------------')
    #         return 1     
        
    #     lista_cadastro = [numero_chip, nome, raca]    

    #     return lista_cadastro

    def gato_ja_cadastrado(self, numero_chip):
        sg.popup(f'O gato com número do chip {numero_chip} já está cadastrado!')

    def sucesso_cadastro_gato(self):
        sg.popup('Gato cadastrado com sucesso!')

    def sem_gatos(self):
        sg.popup('Não existem gatos cadastrados!')

    def mostra_gatos(self, gato):
        sg.popup(gato)

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
