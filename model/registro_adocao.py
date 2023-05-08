from registro import Registro


class RegistroAdocao(Registro):

    def __init__(self, data: str, animal: object, adotante: object, assinou_termo: bool):
        super().__init__(data, animal)
        self.__adotante = adotante
        self.__assinou_termo = assinou_termo

    @property
    def adotante(self):
        return self.__adotante

    @adotante.setter
    def adotante(self, adotante):
        self.__adotante = adotante

    @property
    def assinou_termo(self):
        return self.__assinou_termo

    @assinou_termo.setter
    def assinou_termo(self, assinou_termo):
        self.__assinou_termo = assinou_termo