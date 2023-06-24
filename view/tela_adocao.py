from datetime import date
from PySimpleGUI import PySimpleGUI as sg

class TelaAdocao:

    # TELA DA ÁREA DE ADOÇÃO

    def tela_opcoes_adocao(self):

        self.iniciar_tela()
        button, values = self.__window.Read()
        opcao = 0
        if button == 'Adotar um animal':
            opcao = 1
        if button == 'Listar Adoções':
            opcao = 2
        if button == 'Cadastrar um Adotante':
            opcao = 3
        if button == 'Editar um Adotante':
            opcao = 4
        if button == 'Excluir um Adotante':
            opcao = 5
        if button == 'Listar os Adotantes cadastrados':
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
            [sg.Text('Menu de adoção', size=(50, 1))],
            [sg.Text('O que deseja fazer?')],
            [sg.Button('Adotar um animal', size=(20, 1))],
            [sg.Button('Listar Adoções', size=(20, 1))],
            [sg.Button('Cadastrar um Adotante', size=(20, 1))],
            [sg.Button('Editar um Adotante', size=(20, 1))],
            [sg.Button('Excluir um Adotante', size=(20, 1))],
            [sg.Button('Listar os Adotantes cadastrados', size=(20, 2))],
            [sg.Button('Voltar', size=(20, 1))]
        ]

        self.__window = sg.Window('Ong das Patinhas').Layout(layout)
         
    # ================================


    # LISTA TODAS AS ADOÇÕES REGISTRADAS

    def mostra_adocoes(self, adocoes):
        sg.theme('SandyBeach')
        layout = [[sg.Text('Data da adoção', size=(15, 1)),sg.Text('Nome do Adotante', size=(20, 1)), sg.Text('Numero do chip do animal', size=(20, 1)), sg.Text('Nome do animal', size=(15, 1))]]
        for adocao in adocoes:
            layout.append([sg.Text(adocao.data, size=(15, 1)), sg.Text(adocao.adotante.nome, size=(20, 1)), sg.Text(adocao.animal.numero_chip, size=(20, 1)), sg.Text(adocao.animal.nome, size=(15, 1))])
        layout.append([sg.Button('Voltar', size=(20, 1))])

        
        self.__window = sg.Window('Ong das Patinhas').Layout(layout)

        button, values = self.__window.Read()
        if button == 'Voltar':
            self.close()
            return 1

    # ================================

    def cpf_nao_cadastrado(self, cpf):

        sg.theme('SandyBeach')

        layout = [
            [sg.Text(f'Adotante com CPF {cpf} não cadastrado! Para realizar a adoção é necessário primeiro cadastrar o Adotante')],
            [sg.Text('Deseja realizar um cadastro de adotante??')],
            [sg.Button('Sim', size=(15,1)), sg.Button('Não', size=(15,1))]
        ]

        self.__window = sg.Window('Ong das Patinhas').Layout(layout)

        button, values = self.__window.Read()

        if button == 'Não':
            self.close()
            return 1

        if button == 'Sim':
            self.close()
            return cpf

    def iniciando_adocao(self):
        sg.popup('Cadastro de Adotante encontrado, iniciando adoção!')

    def gato_ou_cachorro(self):
 
        sg.theme('SandyBeach')

        layout = [
            [sg.Text('Bem vindo ao sistema de adoção, deseja adotar um gato ou um cachorro?')],
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
    
    def finalizar_adocao(self):

        data = date.today()
        data_adocao = '{}/{}/{}'.format(data.day, data.month, data.year)

        sg.theme('SandyBeach')

        layout = [
            [sg.Text('Para adotar um animalzinho, é necessário assinar o termo de responsabilidade.')],
            [sg.Text('Deseja assinar o termo?')],
            [sg.Button('Assinar termo', size=(20,1))],
            [sg.Button('Não assinar (cancelará a adoção)', size=(20,2))],
        ]

        self.__window = sg.Window('Ong das Patinhas').Layout(layout)

        button, values = self.__window.Read()

        if button == 'Não assinar (cancelará a adoção)':
            sg.popup('Adoção Cancelada! Retornando a área de adoção.')
            self.close()
            return 1

        if button == 'Assinar termo':
            self.close()
            return data_adocao

    def sucesso_adocao(self, animal):
        sg.popup(f'{animal} adotado com sucesso!')
    
    def erro_falta_vacinas(self, vacinas):

        sg.theme('SandyBeach')

        layout = [
            [sg.Text('Para adotar um animalzinho, é necessário que ele esteja com essas vacinas em dia: ')],
            [sg.Text('Raiva')],
            [sg.Text('Leptospirose')],
            [sg.Text('Hepatite infecciosa')],
            [sg.Text('Atualmente, ele possui apenas essas vacinas: ')]]

        for vacina in vacinas:
            layout.append([sg.Text(vacina.nome_vacina)])

        layout.append([sg.Text('Deseja vaciná-lo(a) com as vacinas faltantes?')])
        layout.append([sg.Button('Sim', size=(15,2)), sg.Button('Não (cancelará a adoção)', size=(15,2))])


        self.__window = sg.Window('Ong das Patinhas').Layout(layout)

        button, values = self.__window.Read()

        if button == 'Não (cancelará a adoção)':
            sg.popup('Adoção Cancelada! Retornando a área de adoção.')
            self.close()
            return 1

        if button == 'Sim':
            self.close()
            return 2

    def erro_tamanho_apartamento(self):
        sg.popup('Um cachorro de porte grande não pode ser adotado por um Adotante que mora em um apartamento pequeno!\nRetornando ao menu de adoções...')

    def sem_registro_adocoes(self):
        sg.popup('Ainda não existe nenhuma adoção registrada!')
