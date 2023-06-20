from PySimpleGUI import PySimpleGUI as sg


class TelaOng:

    def __init__(self):
        self.__window = None
        self.iniciar_tela()

    def tela_opcoes(self):

        self.iniciar_tela()
        button, values = self.__window.Read()
        opcao = 0
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        # cobre os casos de voltar, não clicar em nada e fechar janela, ou clicar cancelar
        if values['0'] or button in (None,'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def close(self):
        self.__window.Close()

    def iniciar_tela(self):

        sg.theme('Reddit')
        layout = [
            [sg.Text('Bem vindo a Ong das Patinhas!', font=("Helvica",25))],
            [sg.Text('O que deseja fazer?', font=("Helvica",25))],
            [sg.Radio('Área de Adoção',"RD1", key='1')],
            [sg.Radio('Área de Doação',"RD1", key='2')],
            [sg.Radio('Animais',"RD1", key='3')],
            [sg.Radio('Finalizar sistema',"RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]

        self.__window = sg.Window('Ong das Patinhas').Layout(layout)
