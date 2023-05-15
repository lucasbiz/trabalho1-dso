from model.usuario_ong import UsuarioOng


class Adotante(UsuarioOng):

    def __init__(self, cpf: int, nome: str, data_nascimento: str, endereco: str, tipo_habitacao: list):
        super().__init__(cpf, nome, data_nascimento, endereco)
        self.__tipo_habitacao = tipo_habitacao


    @property
    def tipo_habitacao(self):
        return self.__tipo_habitacao

    @tipo_habitacao.setter
    def tipo_habitacao(self, tipo_habitacao):
        if isinstance(tipo_habitacao, list):
            self.__tipo_habitacao = tipo_habitacao