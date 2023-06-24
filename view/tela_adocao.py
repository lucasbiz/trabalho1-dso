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

    def iniando_doacao(self):
        sg.popup('Cadastro de Adotante encontrado, iniciando doação!')

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
 

        # print('---------------- Adoção ---------------')
        # print('Bem vindo ao sistema de adoção, vamos primeiro realizar o cadastro do seu bichinho')
        # print('O animal que será adotado é:')
        # print('1 - Gato')
        # print('2 - Cachorro')
        # print('3 - Voltar')
        # opcao = input('Informe a opção escolhida: ')

        # while opcao not in ['1','2','3']:
        #     print('---------------- Adoção ---------------')
        #     print('Opção inválida! Digite o número da opção novamente: ')
        #     print('O animal que será adotado é:')
        #     print('1 - Gato')
        #     print('2 - Cachorro')
        #     print('3 - Voltar')
        #     opcao = input('Informe a opção escolhida: ')

        # return int(opcao)    
    
    def finalizar_adocao(self):
        print('---------------- Adoção ---------------')
        data = date.today()
        data_em_texto = '{}/{}/{}'.format(data.day, data.month, data.year)
        while len(data) != 8:
            print('--------------- Aviso -----------------')
            data = input('Data inválida! Informe a data da adoção (dd/mm/aa): ')
            print('--------------- Aviso -----------------')
        print('Assinar termo de responsabilidade: ')
        print('1 - Assinar')
        print('2 - Não assinar')
        assinar_termo = input('Escolha uma opção ')
        while assinar_termo not in ['1','2']:
            print('Opção inválida!')
            print('Assinar termo de responsabilidade: ')
            print('1 - Assinar')
            print('2 - Não assinar')
            assinar_termo = input('Escolha uma opção ')

        print('---------------- Adoção ---------------')
        return [data, int(assinar_termo)]

    def sucesso_adocao(self, animal):
        print('--------------- Aviso ----------------')
        print(f'{animal} adotado com sucesso!')
        print('--------------- Aviso ----------------')
    
    def adocao_cancelada_termo():
        print('Não é possivel adotar um animal sem assinar o termo, adoção cancelada!')

    def erro_falta_vacinas(self,):

        print('--------------- Aviso ----------------')
        print('O animal escolhido não possui as vacinas necessárias! Deseja vaciná-lo com as faltantes?')
        print('1 - SIM')
        print('2 - NÃO')
        opcao = input('Informe sua escolha: ')
        print('--------------- Aviso ----------------')

        while opcao not in ['1','2']:
            print('--------------- Aviso ----------------')
            print('Opção inválida! Informe novamente.')
            print('O animal escolhido não possui as vacinas necessárias! Deseja vaciná-lo com as faltantes?')
            print('1 - SIM')
            print('2 - NÃO')
            opcao = input('Informe sua escolha: ')
            print('--------------- Aviso ----------------')
        
        return int(opcao)

    def cancelar_adocao_falta_vacinas(self):
        print('--------------- Aviso ----------------')
        print('Um animal precisa de todas as 3 vacinas para poder ser adotado! Adoção cancelada!')
        print('--------------- Aviso ----------------')

    def erro_tamanho_apartamento(self):
        print('--------------- Aviso ----------------')
        print('Um cachorro de porte grande não pode ser adotado por um Adotante que mora em um apartamento pequeno! Retornando ao menu de adoções...')
        print('--------------- Aviso ----------------')
    
    def sem_registro_adocoes(self):
        print('--------------- Aviso ----------------')
        print('Ainda não existe nenhuma adoção registrada!')
        print('--------------- Aviso ----------------')
