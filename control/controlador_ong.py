from view.tela_ong import TelaOng
from controlador_cat import ControladorCat
from controlador_dog import ControladorDog


class ControladorOng():

    def __init__(self):
        self.__controlador_cat = ControladorCat(self)
        self.__controlador_dog = ControladorDog(self)
        self.__tela_ong = TelaOng()