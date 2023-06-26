from PySimpleGUI import PySimpleGUI as sg


class TelaOng:

    def __init__(self):
        self.__window = None
        self.iniciar_tela()

    def tela_opcoes(self):

        self.iniciar_tela()
        button, values = self.__window.Read()
        opcao = 0
        if button == 'Área de Adoção':
            opcao = 1
        if button == 'Área de Doação':
            opcao = 2
        if button == 'Listar Animais':
            opcao = 3
        # cobre os casos de voltar, não clicar em nada e fechar janela, ou clicar cancelar
        if button in (None,'Finalizar sistema'):
            opcao = 0
        self.close()
        return opcao

    def close(self):
        self.__window.Close()

    def iniciar_tela(self):

        sg.theme('SandyBeach')
        layout = [
            [sg.Text('Bem vindo a Ong das Patinhas!', size=(50, 1))],
            [sg.Text('O que deseja fazer?')],
            [sg.Button('Área de Adoção', size=(20, 1))],
            [sg.Button('Área de Doação', size=(20, 1))],
            [sg.Button('Listar Animais', size=(20, 1))],
            [sg.Button('Finalizar sistema', size=(20, 1))],
        ]

        self.__window = sg.Window('Ong das Patinhas').Layout(layout)


    def gato_ou_cachorro(self):
 
        sg.theme('SandyBeach')

        layout = [
            [sg.Text('Deseja listar os gatos ou cachorros')],
            [sg.Button('Gatos', size=(15,1))],
            [sg.Button('Cachorros', size=(15,1))],
            [sg.Button('Voltar', size=(15,1))]
        ]

        self.__window = sg.Window('Ong das Patinhas').Layout(layout)

        button, values = self.__window.Read()

        if button == 'Voltar':
            self.close()
            return 1

        if button == 'Gatos':
            self.close()
            return 2

        if button == 'Cachorros':
            self.close()
            return 3

