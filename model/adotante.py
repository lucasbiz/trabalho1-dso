from usuario_ong import UsuarioOng


class Adotante(UsuarioOng):

    def __init__(self, cpf: int, nome: str, data_nascimento: str, endereco: str, tipo_habilitacao: str, possui_animais: bool):
        super().__init__(cpf, nome, data_nascimento, endereco)
        self.__tipo_habilitacao = tipo_habilitacao
        self.__possui_animais = possui_animais

    @property
    def tipo_habilitacao(self):
        return self.__tipo_habilitacao

    @tipo_habilitacao.setter
    def tipo_habilitacao(self, tipo_habilitacao):
        if isinstance(tipo_habilitacao, str):
            self.__tipo_habilitacao = tipo_habilitacao

    @property
    def possui_animais(self):
        return self.__possui_animais

    @possui_animais.setter
    def possui_animais(self, possui_animais):
        if isinstance(possui_animais, bool):
            self.__possui_animais = possui_animais