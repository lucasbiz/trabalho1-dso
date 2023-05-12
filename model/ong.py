class Ong():

    def __init__(self, nome_ong: str):
        self.__nome_ong = nome_ong

    @property
    def nome_ong(self):
        return self.__nome_ong

    @nome_ong.setter
    def nome_ong(self, nome_ong):
        if isinstance(nome_ong, str):
            self.__nome_ong = nome_ong


