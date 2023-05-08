from abc import ABC, abstractmethod


class Registro(ABC):

    @abstractmethod
    def __init__(self, data: str, animal: object):
        self.__data = data
        self.__animal = animal

    @property
    def animal(self):
        return self.__animal

    @animal.setter
    def animal(self, animal):
        self.__animal = animal

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data