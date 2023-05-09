from view.tela_gato import TelaGato


class ControladorGato():

    def __init__(self, controlador_ong):
        self.__gatos = []
        self.__controlador_ong = controlador_ong
        self.__tela_gato = TelaGato()