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

                # VALIDACAO NUMERO DO CHIP
                if len(values['numero_chip']) < 1:
                    sg.popup('NÚMERO DO CHIP INVÁLIDO')
                    self.__window['numero_chip'].Update('')
                else:
                    try:
                        informacoes_cadastro.append(int(values['numero_chip']))
                    except Exception:
                        sg.popup('NÚMERO DO CHIP INVÁLIDO')
                        self.__window['numero_chip'].Update('')

                # VALIDACAO NOME
                if len(values['nome']) > 50 or len(values['nome']) < 1:
                    sg.popup('NOME INVÁLIDO')
                    self.__window['nome'].Update('')
                else:
                    try:
                        informacoes_cadastro.append(values['nome'])
                    except Exception:
                        sg.popup('NOME INVÁLIDO')
                        self.__window['nome'].Update('')

                # VALIDACAO RACA
                if len(values['raca']) < 1:
                    sg.popup('RAÇA INVÁLIDA')
                    self.__window['raca'].Update('')
                else:
                    try:
                        informacoes_cadastro.append(values['raca'])
                    except Exception:
                        sg.popup('RAÇA INVÁLIDA')
                        self.__window['raca'].Update('')

                # VALIDACAO VACINAS

                if values['vacina_raiva'] == True:

                    if len(values['data_raiva']) == 10:
                        informacoes_cadastro.append([values['vacina_raiva'], values['data_raiva']])

                    else:
                        sg.popup('Data da vacina da Raiva inválida!')
                        self.__window['data_raiva'].Update('')

                if values['vacina_leptospirose'] == True:

                    if len(values['data_leptospirose']) == 10:
                        informacoes_cadastro.append([values['vacina_leptospirose'], values['data_leptospirose']])

                    else:
                        sg.popup('Data da vacina da Leptospirose inválida!')
                        self.__window['data_leptospirose'].Update('')

                if values['vacina_hepatite'] == True:

                    if len(values['data_hepatite']) == 10:
                        informacoes_cadastro.append([values['vacina_hepatite'], values['data_hepatite']])

                    else:
                        sg.popup('Data da vacina da Hepatite inválida!')
                        self.__window['data_hepatite'].Update('') 

            if button == 'Voltar':
                cadastro_finalizado = True
                self.close()
                return 1
        # FIM VALIDAÇÕES, RETORNA LISTA DE INFORMAÇÕES
        cadastro_finalizado = True
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
            [sg.Text('Histórico de Vacinação: ', size=(25, 1))],
            [sg.Text('Selecione as vacinas que o animal já possui e digite as datas de aplicação: ', size=(25, 1))],
            [sg.Text('Vacina', size=(30, 1)), sg.Text('Data (dd/mm/aaaa)', size=(15, 1))],
            [sg.Checkbox('Raiva', key='vacina_raiva', size=(27, 1)), sg.Text('Data: '), sg.InputText(key='data_raiva', size=(15, 1))],
            [sg.Checkbox('Leptospirose', key='vacina_leptospirose', size=(27, 1)), sg.Text('Data: '), sg.InputText(size=(15, 1), key='data_leptospirose')],
            [sg.Checkbox('Hepatite infecciosa', key='vacina_hepatite', size=(27, 1)), sg.Text('Data: '), sg.InputText(size=(15, 1), key='data_hepatite')],
            [sg.Button('Confirmar', size=(20, 1)), sg.Button('Voltar', size=(20, 1))]
        ]

        self.__window = sg.Window('Ong das Patinhas').Layout(layout)

    def mostra_sucesso_cadastro(self, numero_chip):
        sg.popup(f'Gato com número do chip {numero_chip} cadastrado com sucesso!')

    # fecha a tela 
    def close(self):
        self.__window.Close()

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
