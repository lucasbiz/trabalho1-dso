from view.tela_adotante import TelaAdotante


class ControladorAdotante():

    def __init__(self, controlador_ong):
        self.__adotantes = []
        self.__controlador_ong = controlador_ong
        self.__tela_adotante = TelaAdotante()