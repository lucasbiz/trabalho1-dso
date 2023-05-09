from view.tela_adocao import TelaAdocao


class ControladorAdocao():

    def __init__(self, controlador_ong):
        self.__adocoes = []
        self.__controlador_ong = controlador_ong
        self.__tela_adocoes = TelaAdocao()