from view.tela_ong import TelaOng
from control.controlador_adocao import ControladorAdocao
from control.controlador_adotante import ControladorAdotante
from control.controlador_cachorro import ControladorCachorro
from control.controlador_doacao import ControladorDoacao
from control.controlador_doador import ControladorDoador
from control.controlador_gato import ControladorGato


class ControladorOng():

    def __init__(self):
        self.__controlador_adocao = ControladorAdocao(self)
        self.__controlador_adotante = ControladorAdotante(self)
        self.__controlador_Cachorro = ControladorCachorro(self)
        self.__controlador_doacao = ControladorDoacao(self)
        self.__controlador_doador = ControladorDoador(self)
        self.__controlador_Gato = ControladorGato(self)
        self.__tela_ong = TelaOng()

    def inicia_sistema(self):
        self.mostra_tela()

    def consultar_doacoes(self):
        self.__controlador_doacao.mostra_tela_consulta()

    def consultar_adocoes(self):
        print('DEU CERTO 2')

    def doar(self):
        self.__controlador_doacao.mostra_tela_doacao()

    def adotar(self):
        print('DEU CERTO 4')
    
    def listar_doadores(self):
        self.__controlador_doador.listar_doadores()

    def listar_adotantes(self):
        print('ADOTANTES AQUI')

    def finalizar(self):
        exit(0)

    def mostra_tela(self):
        lista_opcoes = {1: self.consultar_doacoes, 2: self.consultar_adocoes, 3: self.doar, 4: self.adotar, 5: self.listar_doadores, 6: self.listar_adotantes, 7: self.finalizar}
        #colocar uma opcao de finalizar sistema usando exit
        while True:
            opcao_escolhida = self.__tela_ong.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()