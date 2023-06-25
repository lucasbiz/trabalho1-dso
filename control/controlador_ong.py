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

    # def consultar_doacoes(self):
    #     self.__controlador_doacao.mostra_tela_consulta()

    # def consultar_adocoes(self):
    #     self.__controlador_adocao.mostra_tela_consulta()

    # def doar(self):
    #     self.__controlador_doacao.mostra_tela_doacao()

    # def adotar(self):
    #     self.__controlador_adocao.mostra_tela_adocao()
    
    # def listar_doadores(self):
    #     self.__controlador_doacao.listar_doadores()
    
    def pegar_doadores(self):
        chaves_doadores = self.__controlador_doacao.pegar_doadores()
        return chaves_doadores

    # def listar_adotantes(self):
    #     self.__controlador_adocao.listar_adotantes()

    # def listar_animais(self):
    #     self.__controlador_doacao.listar_animais()

    def area_adocao(self):
        self.__controlador_adocao.mostra_tela_adocao()

    def area_doacao(self):
        self.__controlador_doacao.mostra_tela_doacao()


    def area_animais(self):
        # cadastrar animal
        # editar um animal
        # excluir um animal
        print('AREA ANIMAIS')

    def finalizar(self):
        exit(0)

    def mostra_tela(self):
        lista_opcoes = {1: self.area_adocao, 2: self.area_doacao, 3: self.area_animais, 0: self.finalizar}

        opcao_escolhida = self.__tela_ong.tela_opcoes()
        funcao_escolhida = lista_opcoes[opcao_escolhida]
        funcao_escolhida()
