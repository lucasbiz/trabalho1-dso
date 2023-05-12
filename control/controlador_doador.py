from view.tela_doador import TelaDoador
from model.doador import Doador

class ControladorDoador():

    def __init__(self, controlador_ong):
        self.__doadores = {}
        self.__controlador_ong = controlador_ong
        self.__tela_doador = TelaDoador()

    def cadastrar_doador(self):
        self.tela_cadastro()
    
    def cancelar_cadastro(self):
        self.__controlador_ong.doar()

    def tela_cadastro(self):

        opcao_escolhida = self.__tela_doador.mostra_tela_cadastro()
        print(opcao_escolhida)

        if opcao_escolhida == 1:
            self.cancelar_cadastro

        elif isinstance(opcao_escolhida, list):
            doador = Doador(opcao_escolhida[0], opcao_escolhida[1], opcao_escolhida[2], opcao_escolhida[3])
            self.__doadores[opcao_escolhida[0]] = doador
            self.__tela_doador.mostra_sucesso_cadastro(opcao_escolhida[0])