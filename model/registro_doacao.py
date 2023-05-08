from registro import Registro


class RegistroDoacao(Registro):

    def __init__(self, data: str, animal: object, doador: object, motivo: str):
        super().__init__(data, animal)
        self.__doador = doador
        self.__motivo = motivo

    @property
    def doador(self):
        return self.__doador

    @doador.setter
    def doador(self, doador):
        if isinstance(doador, object):
            self.__doador = doador

    @property
    def motivo(self):
        return self.__motivo

    @motivo.setter
    def motivo(self, motivo):
        if isinstance(motivo, str):
            self.__motivo = motivo