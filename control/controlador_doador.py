from view.tela_doador import TelaDoador


class ControladorDoador():

    def __init__(self, controlador_ong):
        self.__doadores = []
        self.__controlador_ong = controlador_ong
        self.__tela_doador = TelaDoador()