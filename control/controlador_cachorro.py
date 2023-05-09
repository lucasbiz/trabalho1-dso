from view.tela_cachorro import TelaCachorro


class ControladorCachorro():

    def __init__(self, controlador_ong):
        self.__cachorros = []
        self.__controlador_ong = controlador_ong
        self.__tela_cachorro = TelaCachorro()