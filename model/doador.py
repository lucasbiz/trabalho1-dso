from usuario_ong import UsuarioOng


class Doador(UsuarioOng):

    def __init__(self, cpf: int, nome: str, data_nascimento: str, endereco: str):
        super().__init__(cpf, nome, data_nascimento, endereco)