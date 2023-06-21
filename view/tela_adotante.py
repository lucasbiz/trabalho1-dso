from PySimpleGUI import PySimpleGUI as sg


class TelaAdotante:


# ============= CADASTRO E VALIDAÇÕES =================

    def mostra_tela_cadastro(self):

        cadastro_finalizado = False
        informacoes_cadastro = []
        self.iniciar_tela()

        while cadastro_finalizado == False:
            button, values = self.__window.Read()
            opcao = 0

            if button == 'Confirmar':

                # VALIDACAO CPF
                if len(values['cpf']) != 11:
                    sg.popup('CPF INVÁLIDO')
                    self.__window['cpf'].Update('')
                else:
                    try:
                        int(values['cpf'])
                        informacoes_cadastro.append(values['cpf'])
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

                # VALIDACAO TIPO DE HABITACAO
                menu_dropdown_habitacao = ['Casa Pequena', 'Casa média', 'Casa grande', 'Apartamento pequeno', 'Apartamento médio', 'Apartamento grande']
                if values['tipo_habitacao'] not in menu_dropdown_habitacao:
                    sg.popup(values['TIPO DE HABITAÇÃO INVÁLIDA'])
                    self.__window['tipo_habitacao'].Update('')
                else:
                    try:
                        informacoes_cadastro.append(values['tipo_habitacao'])
                    except Exception:
                        sg.popup('TIPO DE HABITAÇÃO INVÁLIDA')
                        self.__window['tipo_habitacao'].Update('')

                cadastro_finalizado = True

            if button == 'Voltar':
                cadastro_finalizado = True
                self.close()
                return 1
        # FIM VALIDAÇÕES, RETORNA LISTA DE INFORMAÇÕES
        return informacoes_cadastro

    # fecha a tela 
    def close(self):
        self.__window.Close()

    # Tela de cadastro de novo adotante
    def iniciar_tela(self):

        sg.theme('SandyBeach')

        menu_dropdown_habitacao = ['Casa Pequena', 'Casa média', 'Casa grande', 'Apartamento pequeno', 'Apartamento médio', 'Apartamento grande']

        layout = [
            [sg.Text('Cadastro de novo Adotante', size=(50, 1))],
            [sg.Text('Informe seus dados para prosseguir:')],
            [sg.Text('CPF: ', size=(25, 1)), sg.InputText(key='cpf', size=(20, 1))],
            [sg.Text('Nome: ', size=(25, 1)), sg.InputText(key='nome', size=(20, 1))],
            [sg.Text('Data de Nascimento(dd/mm/aaaa)', size=(25, 1)), sg.InputText(key='data_nascimento', size=(20, 1))],
            [sg.Text('Endereço: ', size=(25, 1)), sg.InputText(key='endereco', size=(20, 1))],
            [sg.Text('Tipo de Habitação: ', size=(25, 1)), sg.DropDown(menu_dropdown_habitacao, size=(20), key=('tipo_habitacao'))],
            [sg.Button('Confirmar', size=(20, 1)), sg.Button('Voltar', size=(20, 1))]
        ]

        self.__window = sg.Window('Ong das Patinhas').Layout(layout)


    def mostra_sucesso_cadastro(self, cpf):
        print(f'Adotante com CPF: {cpf} cadastrado com sucesso!')

# ==================== FIM CADASTRO ====================


    def mostra_adotantes(self, adotante):
        print(adotante)

    def sem_adotantes(self):
        print('Não existem adotantes cadastrados!')

    def cpf_ja_cadastrado(self, cpf):
        print('--------------- Aviso ---------------')
        print(f'CPF {cpf} já cadastrado como adotante!')
        print('--------------- Aviso ---------------')
    
    def cpf_nao_encontrado(self, cpf):
        print('--------------- Aviso ---------------')
        print(f'CPF {cpf} não encontrado!')
        print('--------------- Aviso ---------------')
    
    def cpf_ja_cadastrado_doador(self, cpf):
        print(f'CPF {cpf} já cadastrado como doador!')
        print('--------------- Aviso ---------------')
