from view.tela_ong import TelaOng
from control.controlador_adocao import ControladorAdocao
from control.controlador_adotante import ControladorAdotante
from control.controlador_cachorro import ControladorCachorro
from control.controlador_doacao import ControladorDoacao
from control.controlador_gato import ControladorGato


class ControladorOng():

    def __init__(self):
        self.__controlador_adocao = ControladorAdocao(self)
        self.__controlador_adotante = ControladorAdotante(self)
        self.__controlador_Cachorro = ControladorCachorro(self)
        self.__controlador_doacao = ControladorDoacao(self)
        self.__controlador_Gato = ControladorGato(self)
        self.__tela_ong = TelaOng()

    def inicia_sistema(self):
        self.mostra_tela()

    def consultar_doacoes(self):
        self.__controlador_doacao.mostra_tela_consulta()

    def consultar_adocoes(self):
        pass

    def doar(self):
        self.__controlador_doacao.mostra_tela_doacao()

    def adotar(self):
        pass
    
    def listar_doadores(self):
        self.__controlador_doacao.listar_doadores()

    def listar_adotantes(self):
        pass

    def finalizar(self):
        exit(0)

    def mostra_tela(self):
        lista_opcoes = {1: self.consultar_doacoes, 2: self.consultar_adocoes, 3: self.listar_doadores, 4: self.listar_adotantes, 5: self.doar, 6: self.adotar, 7: self.finalizar}
        #colocar uma opcao de finalizar sistema usando exit
        while True:
            opcao_escolhida = self.__tela_ong.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()