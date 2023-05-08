from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def __init__(self, numero_chip: int, nome: str, raca: str, historico_vacinacao: list):
        self.__numero_chip = numero_chip
        self.__nome = nome
        self.__raca = raca
        self.__historico_vacinacao = historico_vacinacao

    @property
    def numero_chip(self):
        return self.__numero_chip

    @numero_chip.setter
    def numero_chip(self, numero_chip):
        self.__numero_chip = numero_chip

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def raca(self):
        return self.__raca

    @raca.setter
    def raca(self, raca):
        self.__raca = raca

    @property
    def historico_vacinacao(self):
        return self.__historico_vacinacao

    @historico_vacinacao.setter
    def historico_vacinacao(self, historico_vacinacao):
        self.__historico_vacinacao = historico_vacinacao

# se "vacinar" estará no controlador, precisa entrar aqui?