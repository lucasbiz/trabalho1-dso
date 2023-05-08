from ..view.tela_ong import TelaOng
from controlador_gato import ControladorGato
from controlador_cachorro import ControladorCachorro


class ControladorOng():

    def __init__(self):
        self.__controlador_cat = ControladorGato(self)
        self.__controlador_dog = ControladorCachorro(self)
        self.__tela_ong = TelaOng()

    def inicia_sistema(self):
        self.mostra_tela()

    def consultar_doacoes(self):
        print('DEU CERTO')

    def mostra_tela(self):
        lista_opcoes = {1: self.consultar_doacoes, 2: self.opcao2, 3: self.opcao3, 4: self.opcao4}
        
        while True:
            opcao_escolhida = self.__tela_ong.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()