from PySimpleGUI import PySimpleGUI as sg

class TelaCachorro:

    def cachorro_ja_cadastrado(self, numero_chip):
        sg.popup(f'O cachorro com número do chip {numero_chip} já está cadastrado!')

    def mostra_tela_cadastro(self):
        print('--------------- Cadastrar Cachorro ---------------')
        print('Informe seus dados para realizar o cadastro!: ')

        try:
            numero_chip = int(input('Digite o NÚMERO DO CHIP do Cachorro ou 1 para cancelar: '))
            if numero_chip == 1:
                return 1    
        except Exception:
            print('--------------- Número inválido! revise os dados e tente novamente. ---------------')
            return 1
        try:
            nome = input('Digite o NOME do cachorro ou 1 para cancelar: ')
            if nome == '1':
                return 1
        except Exception:
            print('--------------- NOME inválido! revise seus dados e tente novamente. ---------------')
            return 1    

        try:
            raca = input('Digite a RAÇA do Cachorro ou 1 para cancelar: ')
            if raca == '1':
                return 1
        except Exception:
            print('--------------- RAÇA inválida! revise seus dados e tente novamente. ---------------')
            return 1    

        try:
            tamanho = input('Digite o TAMANHO do Cachorro (1 - pequeno/ 2 - medio/ 3 - grande) ou 4 para cancelar: ')
            if tamanho == '4' or tamanho not in ['1','2','3']:
                return 1
        except Exception:
            print('--------------- TAMANHO inválido! revise seus dados e tente novamente. ---------------')
            return 1    
        
        lista_cadastro = [numero_chip, nome, raca, int(tamanho)]    

        return lista_cadastro
    
    def sucesso_cadastro_cachorro(self):
        sg.popup('Cachorro cadastrado com sucesso!')
    
    def sem_cachorros(self):
        sg.popup('Não existem cachorros cadastrados!')

    def mostra_cachorros(self, cachorro):
        print(cachorro)

    def cachorro_nao_encontrado(self):
        sg.popup('CACHORRO NÃO ENCONTRADO')

    def pegar_cachorro_pelo_numero(self):

        sg.theme('SandyBeach')
        layout = [[sg.Text(f'Informe o número do chip do cachorro desejado: '), sg.InputText(key='numero_chip', size=(15,1))]]
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
                    sg.popup('Cachorro encontrado! Prosseguindo adoção...')
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
