from PySimpleGUI import PySimpleGUI as sg

class TelaDoador:

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

                if len(informacoes_cadastro) == 4:
                    cadastro_finalizado = True

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
            [sg.Text('Cadastro de novo Doador', size=(50, 1))],
            [sg.Text('Informe seus dados para prosseguir:')],
            [sg.Text('CPF: ', size=(25, 1)), sg.InputText(key='cpf', size=(20, 1))],
            [sg.Text('Nome: ', size=(25, 1)), sg.InputText(key='nome', size=(20, 1))],
            [sg.Text('Data de Nascimento(dd/mm/aaaa)', size=(25, 1)), sg.InputText(key='data_nascimento', size=(20, 1))],
            [sg.Text('Endereço: ', size=(25, 1)), sg.InputText(key='endereco', size=(20, 1))],
            [sg.Button('Confirmar', size=(20, 1)), sg.Button('Voltar', size=(20, 1))]
        ]

        self.__window = sg.Window('Ong das Patinhas').Layout(layout)

    def mostra_sucesso_cadastro(self, cpf):
        sg.popup(f'Adotante com CPF {cpf} cadastrado com sucesso!')

    # fecha a tela 
    def close(self):
        self.__window.Close()

    def mostra_doadores(self, doadores):

        sg.theme('SandyBeach')
        layout = [[sg.Text('Nome', size=(20, 1)),sg.Text('CPF', size=(15, 1)),sg.Text('Endereço', size=(20, 1))]]
        for doador in doadores:
            layout.append([sg.Text(doador.nome, size=(20, 1)),sg.Text(doador.cpf, size=(15, 1)),sg.Text(doador.endereco)])
        layout.append([sg.Button('Voltar', size=(20, 1))])

        
        self.__window = sg.Window('Ong das Patinhas').Layout(layout)

        button, values = self.__window.Read()
        if button == 'Voltar':
            self.close()
            return 1

    def informe_cpf(self):

        sg.theme('SandyBeach')
        layout = [[sg.Text(f'Informe o CPF do Doador: ', size=(20, 1)), sg.InputText(key='cpf', size=(15,1))]]
        layout.append([sg.Button('Confirmar', size=(20, 1)), sg.Button('Voltar', size=(20, 1))])

        
        self.__window = sg.Window('Ong das Patinhas').Layout(layout)

        cpf_correto = False

        while cpf_correto == False:

            button, values = self.__window.Read()
            if button == 'Confirmar':
                # VALIDACAO CPF
                if len(values['cpf']) != 11:
                    sg.popup('CPF INVÁLIDO')
                    self.__window['cpf'].Update('')
                else:
                    try:
                        cpf = int(values['cpf'])
                        cpf_correto = True
                        self.close()
                        return cpf

                    except Exception:
                        sg.popup('CPF INVÁLIDO')
                        self.__window['cpf'].Update('')
                

            if button == 'Voltar':
                cpf_correto = True
                self.close()
                return 1

    def tela_edicao_doador(self, doador):

        sg.theme('SandyBeach')

        layout = [
            [sg.Text('Edição de doador', size=(50, 1))],
            [sg.Text('Informe os novos dados para prosseguir:')],
            [sg.Text('CPF: ', size=(25, 1)), sg.InputText(doador.cpf ,key='cpf', size=(20, 1))],
            [sg.Text('Nome: ', size=(25, 1)), sg.InputText(doador.nome ,key='nome', size=(20, 1))],
            [sg.Text('Data de Nascimento(dd/mm/aaaa)', size=(25, 1)), sg.InputText(doador.data_nascimento, key='data_nascimento', size=(20, 1))],
            [sg.Text('Endereço: ', size=(25, 1)), sg.InputText(doador.endereco, key='endereco', size=(20, 1))],
            [sg.Button('Confirmar', size=(20, 1)), sg.Button('Voltar', size=(20, 1))]
        ]

        self.__window = sg.Window('Ong das Patinhas').Layout(layout)

        informacoes_cadastro_edicao = self.validacoes_cadastro()
        return informacoes_cadastro_edicao

    def mostra_sucesso_edicao(self, cpf):
        sg.popup(f'Doador com cpf {cpf} editado com sucesso!')

    def sem_doadores(self):
        sg.popup('Não existem doadores cadastrados!')

    def cpf_ja_cadastrado(self, cpf):
        sg.popup(f'CPF {cpf} já cadastrado como doador!')
    
    def cpf_nao_encontrado(self, cpf):
        sg.popup(f'CPF {cpf} não encontrado!')

    def mostra_sucesso_edicao(self, cpf):
        sg.popup(f'Doador com cpf {cpf} editado com sucesso!')

    def doador_removido_sucesso(self, cpf):
        sg.popup(f'Doador com CPF {cpf} foi removido com sucesso!')

