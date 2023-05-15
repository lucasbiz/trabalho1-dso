class TelaVacina:

    def mostra_tela_vacinacao(self):
        vacina = []
        print('---------------- Vacinação ---------------')
        print('Quais vacinas seu animal já possui? Informe o número correspondente: ')
        print('1 - Raiva ')
        print('2 - Leptospirose')
        print('3 - Hepatite Infecciosa')
        print('4 - Nenhuma/Voltar')
        opcao = input('Informe a vacina: ')
        print('---------------- Vacinação ---------------')

        while opcao not in ['1','2','3','4']:
            print('---------------- Vacinação ---------------')
            print('Opção inválida! tente novamente')
            print('Quais vacinas seu animal já possui? Informe o número correspondente: ')
            print('1 - Raiva ')
            print('2 - Leptospirose')
            print('3 - Hepatite Infecciosa')
            print('4 - Nenhuma/Voltar')
            opcao = input('Informe a vacina: ')
            print('---------------- Vacinação ---------------')

        if int(opcao) == 4:
            return 1

        print('---------------- Vacinação ---------------')
        data_vacina = input('Informe a data da aplicação dessa vacina (dd/mm/aa): ')
        print('---------------- Vacinação ---------------')    
        
        while len(data_vacina) != 8:
            print('---------------- Vacinação ---------------')
            data_vacina = input('Data de aplicação inválida! Informe novamente (dd/mm/aa): ')
            print('---------------- Vacinação ---------------')

        if int(opcao) == 1:
            opcao = 'Raiva'
        elif int(opcao) == 2:
            opcao = 'Leptospirose'
        elif int(opcao) == 3:
            opcao = 'Hepatite Infecciosa'

        vacina.append(opcao)
        vacina.append(data_vacina)

        return vacina
    
    def confirma_vacina(self):
        print('---------------- Vacinação ---------------')
        print('Deseja adicionar mais alguma vacina?')
        print('1 - SIM ')
        print('2 - NÂO')
        opcao = input('Informe a opção escolhida: ')
        print('---------------- Vacinação ---------------')

        while opcao not in ['1','2']:
            print('---------------- Vacinação ---------------')
            print('Opção inválida! Deseja adicionar mais alguma vacina?')
            print('1 - SIM ')
            print('2 - NÂO')
            opcao = input('Informe a opção escolhida: ')
            print('---------------- Vacinação ---------------')
        
        return int(opcao)