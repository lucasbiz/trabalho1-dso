from abc import ABC, abstractmethod


class UsuarioOng(ABC):

    @abstractmethod
    def __init__(self, cpf: int, nome: str, data_nascimento: str, endereco: str ):
        self.__cpf = cpf
        self.__nome = nome
        self.__data_nascimento = data_nascimento
        self.__endereco = endereco

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        if isinstance(cpf, int):
            self.__cpf = cpf

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str):
            self.__nome = nome

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento):
        if isinstance(data_nascimento, str):
            self.__data_nascimento = data_nascimento

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco):
        if isinstance(endereco, str):
            self.__endereco = endereco