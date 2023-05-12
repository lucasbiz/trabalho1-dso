from view.tela_doacao import TelaDoacao
from control.controlador_doador import ControladorDoador

class ControladorDoacao():

    def __init__(self, controlador_ong):
        self.__doacoes = ['Doacao1', 'Doacao2']
        self.__controlador_ong = controlador_ong
        self.__controlador_doador = ControladorDoador(self)
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

        opcao_escolhida = self.__tela_doacao.tela_opcoes_doacao()
        funcao_escolhida = lista_opcoes[opcao_escolhida]
        funcao_escolhida()

    def cadastra_doador(self):
        self.__controlador_doador.cadastrar_doador()
        #self.__controlador_doador.listar_doadores()
        # chamar o controlador_doador
        # abrir uma tela para colocar os dados com opcao de voltar
        # mostrar uma tela para conferir se os dados tao corretos?
        # averiguar se na lista de doadores nao tem nenhum igual
        # averiguar se o doador nao é também um adotante, só pode ser um ou outro
        pass

    def doar(self):

        # opcoes - cadastrar doador e doar animal
        # se quiser doar, tem que verificar se possui cadastro, se nao, jogar na tela de cadastro
        # se quiser apenas cadastrar, executar o cadastro e voltar a tela de doacao, com opcao voltar
        pass

    def listar_doadores(self):
        self.__controlador_doador.listar_doadores()
