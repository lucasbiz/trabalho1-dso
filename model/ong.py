class Ong():

    def __init__(self, nome_ong: str):
        self.__nome_ong = nome_ong
        self.__doacoes = []
        self.__adocoes = []
        self.__doadores = []
        self.__adotantes = []

    @property
    def nome_ong(self):
        return self.__nome_ong

    @nome_ong.setter
    def nome_ong(self, nome_ong):
        if isinstance(nome_ong, str):
            self.__nome_ong = nome_ong

    @property
    def doacoes(self):
        return self.__doacoes

    @property
    def adocoes(self):
        return self.__adocoes

    @property
    def doadores(self):
        return self.__doadores

    @property
    def adotantes(self):
        return self.__adotantes
