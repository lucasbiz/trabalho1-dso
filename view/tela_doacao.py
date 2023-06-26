from PySimpleGUI import PySimpleGUI as sg

class TelaDoacao:

    def tela_opcoes_doacao(self):

        self.iniciar_tela()
        button, values = self.__window.Read()
        opcao = 0
        if button == 'Doar um animal':
            opcao = 1
        if button == 'Listar Doações':
            opcao = 2
        if button == 'Cadastrar um Doador':
            opcao = 3
        if button == 'Editar um Doador':
            opcao = 4
        if button == 'Excluir um Doador':
            opcao = 5
        if button == 'Listar os Doadores cadastrados':
            opcao = 6
        if button == 'Voltar':
            opcao = 7
        self.close()
        return opcao

    def close(self):
        self.__window.Close()

    def iniciar_tela(self):

        sg.theme('SandyBeach')
        layout = [
            [sg.Text('Menu de doação', size=(50, 1))],
            [sg.Text('O que deseja fazer?')],
            [sg.Button('Doar um animal', size=(20, 1))],
            [sg.Button('Listar Doações', size=(20, 1))],
            [sg.Button('Cadastrar um Doador', size=(20, 1))],
            [sg.Button('Editar um Doador', size=(20, 1))],
            [sg.Button('Excluir um Doador', size=(20, 1))],
            [sg.Button('Listar os Doadores cadastrados', size=(20, 2))],
            [sg.Button('Voltar', size=(20, 1))]
        ]

        self.__window = sg.Window('Ong das Patinhas').Layout(layout)
         
    # ================================

    def mostra_doacoes(self, doacoes):

        sg.theme('SandyBeach')
        layout = [[sg.Text('Data da doação', size=(15, 1)),sg.Text('Nome do Doador', size=(20, 1)), sg.Text('Numero do chip do animal', size=(20, 1)), sg.Text('Nome do animal', size=(15, 1))]]
        for doacao in doacoes:
            layout.append([sg.Text(doacao.data, size=(15, 1)), sg.Text(doacao.doador.nome, size=(20, 1)), sg.Text(doacao.animal.numero_chip, size=(20, 1)), sg.Text(doacao.animal.nome, size=(15, 1))])
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


    def cpf_nao_cadastrado(self, cpf):

        sg.theme('SandyBeach')

        layout = [
            [sg.Text(f'Doador com CPF {cpf} não cadastrado! Para realizar a adoção é necessário primeiro cadastrar o Doador')],
            [sg.Text('Deseja realizar um cadastro de doador?')],
            [sg.Button('Sim', size=(15,1)), sg.Button('Não', size=(15,1))]
        ]

        self.__window = sg.Window('Ong das Patinhas').Layout(layout)

        button, values = self.__window.Read()

        if button == 'Não':
            self.close()
            return 1

        if button == 'Sim':
            self.close()
            return 2

    def gato_ou_cachorro(self):
 
        sg.theme('SandyBeach')

        layout = [
            [sg.Text('Bem vindo ao sistema de doação, deseja doar um gato ou um cachorro?')],
            [sg.Button('Gato', size=(15,1))],
            [sg.Button('Cachorro', size=(15,1))],
            [sg.Button('Voltar', size=(15,1))]
        ]

        self.__window = sg.Window('Ong das Patinhas').Layout(layout)

        button, values = self.__window.Read()

        if button == 'Voltar':
            self.close()
            return 1

        if button == 'Gato':
            self.close()
            return 2

        if button == 'Cachorro':
            self.close()
            return 3 

    def sucesso_doacao(self, animal):
        sg.popup(f'{animal.nome} doado com sucesso!')

    def sem_registro_doacoes(self):
        sg.popup('Ainda não existe nenhuma doação registrada!')

    def iniciando_doacao(self):
        sg.popup('Cadastro de Doador encontrado, iniciando doação!')

    def pedir_motivo(self):

        sg.theme('SandyBeach')
        layout = [[sg.Text(f'Informe o motivo da doação: ', size=(20, 1)), sg.InputText(key='motivo', size=(15,1))]]
        layout.append([sg.Button('Confirmar', size=(20, 1)), sg.Button('Cancelar', size=(20, 1))])

        
        self.__window = sg.Window('Ong das Patinhas').Layout(layout)

        motivo_correto = False

        while motivo_correto == False:

            button, values = self.__window.Read()
            if button == 'Confirmar':
                # VALIDACAO motivo
                if len(values['motivo']) < 1:
                    sg.popup('MOTIVO INVÁLIDO')
                    self.__window['motivo'].Update('')
                else:
                    try:
                        motivo = values['motivo']
                        motivo_correto = True
                        self.close()
                        return motivo

                    except Exception:
                        sg.popup('MOTIVO INVÁLIDO')
                        self.__window['motivo'].Update('')

            if button == 'Cancelar':
                motivo_correto = True
                self.close()
                return 1
