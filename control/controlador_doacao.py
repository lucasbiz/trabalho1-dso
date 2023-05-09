from view.tela_doacao import TelaDoacao


class ControladorDoacao():

    def __init__(self, controlador_ong):
        self.__doacoes = ['Doacao1', 'Doacao2']
        self.__controlador_ong = controlador_ong
        self.__tela_doacao = TelaDoacao()


    #consulta de doacoes

    def mostra_doacoes(self):
        for doacao in self.__doacoes:
            self.__tela_doacao.mostra_doacoes(doacao) #serao objetos que passarao por aqui, ai vai ter que incluir seus atributos no print

    def mostra_doacoes_periodo(self):
        pass

    def voltar(self):
        self.__controlador_ong.mostra_tela()

    def mostra_tela_consulta(self):
        lista_opcoes = {1:self.mostra_doacoes, 2: self.mostra_doacoes_periodo, 3: self.voltar}

        opcao_escolhida = self.__tela_doacao.tela_opcoes_consulta()
        funcao_escolhida = lista_opcoes[opcao_escolhida]
        funcao_escolhida()

  
    #doacoes

    def mostra_tela_doacao(self):
        lista_opcoes = {1:self.doar, 2: self.cadastra_doador, 3: self.voltar}

        opcao_escolhida = self.__tela_doacao.tela_opcoes_consulta()
        funcao_escolhida = lista_opcoes[opcao_escolhida]
        funcao_escolhida()

    def cadastra_doador(self):
        pass

    def doar(self):

        # opcoes - cadastrar doador e doar animal
        # se quiser doar, tem que verificar se possui cadastro, se nao, jogar na tela de cadastro
        # se quiser apenas cadastrar, executar o cadastro e voltar a tela de doacao, com opcao voltar
        pass
