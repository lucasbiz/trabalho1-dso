from view.tela_ong import TelaOng
from control.controlador_gato import ControladorGato
from control.controlador_cachorro import ControladorCachorro


class ControladorOng():

    def __init__(self):
        self.__controlador_Gato = ControladorGato(self)
        self.__controlador_Cachorro = ControladorCachorro(self)
        self.__doacoes = []
        self.__adocoes = []
        self.__tela_ong = TelaOng()

    def inicia_sistema(self):
        self.mostra_tela()

    def consultar_doacoes(self):
        for animal in self.__doacoes:
            self.__tela_ong.mostra_doacao(animal)

    def consultar_adocoes(self):
        print('DEU CERTO 2')

    def doar(self):
        print('DEU CERTO 3')

    def adotar(self):
        print('DEU CERTO 4')

    def finalizar(self):
        exit(0)

    def mostra_tela(self):
        lista_opcoes = {1: self.consultar_doacoes, 2: self.consultar_adocoes, 3: self.doar, 4: self.adotar, 5: self.finalizar}
        #colocar uma opcao de finalizar sistema usando exit
        while True:
            opcao_escolhida = self.__tela_ong.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()