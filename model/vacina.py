class Vacina():

    def __init__(self, nome_vacina: str, data_aplicacao: str):
        self.__nome_vacina = nome_vacina
        self.__data_aplicacao = data_aplicacao

    @property
    def nome_vacina(self):
        return self.__nome_vacina

    @nome_vacina.setter
    def nome_vacina(self, nome_vacina):
        self.__nome_vacina = nome_vacina

    @property
    def data_aplicacao(self):
        return self.__data_aplicacao

    @data_aplicacao.setter
    def data_aplicacao(self, data_aplicacao):
        self.__data_aplicacao = data_aplicacao