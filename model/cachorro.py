from model.animal import Animal


class Cachorro(Animal):

    def __init__(self, numero_chip: int, nome: str, raca: str, historico_vacinacao: list, tamanho: int):
        super().__init__(numero_chip, nome, raca, historico_vacinacao)
        self.__tamanho = tamanho

    @property
    def tamanho(self):
        return self.__tamanho

    @tamanho.setter
    def tamanho(self, tamanho):
        if isinstance(tamanho, str):
            self.__tamanho = tamanho
