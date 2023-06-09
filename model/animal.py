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
        if isinstance(numero_chip, int):
            self.__numero_chip = numero_chip

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str):
            self.__nome = nome

    @property
    def raca(self):
        return self.__raca

    @raca.setter
    def raca(self, raca):
        if isinstance(raca, str):
            self.__raca = raca

    @property
    def historico_vacinacao(self):
        return self.__historico_vacinacao

    @historico_vacinacao.setter
    def historico_vacinacao(self, historico_vacinacao):
        if isinstance(historico_vacinacao, list):
            self.__historico_vacinacao = historico_vacinacao

