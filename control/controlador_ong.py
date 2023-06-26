from view.tela_ong import TelaOng
from control.controlador_adocao import ControladorAdocao
from control.controlador_doacao import ControladorDoacao


class ControladorOng():

    def __init__(self):
        self.__controlador_adocao = ControladorAdocao(self)
        self.__controlador_doacao = ControladorDoacao(self)
        self.__tela_ong = TelaOng()

    def inicia_sistema(self):
        self.mostra_tela()
    
    def pegar_doadores(self):
        chaves_doadores = self.__controlador_doacao.pegar_doadores()
        return chaves_doadores

    def listar_adotantes(self):
        self.__controlador_adocao.listar_adotantes()

    def verificar_adotantes(self):
        return self.__controlador_adocao.verificar_adotantes()

    def area_adocao(self):
        self.__controlador_adocao.mostra_tela_adocao()

    def area_doacao(self):
        self.__controlador_doacao.mostra_tela_doacao()


    def listar_animais(self):
        opcao_gato_ou_cachorro = self.__tela_ong.gato_ou_cachorro()
        if opcao_gato_ou_cachorro == 1:
            self.mostra_tela()

        if opcao_gato_ou_cachorro == 2:
            self.__controlador_doacao.listar_animais(2)
            self.listar_animais()

        if opcao_gato_ou_cachorro == 3:
            self.__controlador_doacao.listar_animais(3)
            self.listar_animais()

    def finalizar(self):
        exit(0)

    def mostra_tela(self):
        lista_opcoes = {1: self.area_adocao, 2: self.area_doacao, 3: self.listar_animais, 0: self.finalizar}

        opcao_escolhida = self.__tela_ong.tela_opcoes()
        funcao_escolhida = lista_opcoes[opcao_escolhida]
        funcao_escolhida()
