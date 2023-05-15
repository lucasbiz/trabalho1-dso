from model.usuario_ong import UsuarioOng


class Adotante(UsuarioOng):

    def __init__(self, cpf: int, nome: str, data_nascimento: str, endereco: str, tipo_habitacao: str, possui_animais: bool):
        super().__init__(cpf, nome, data_nascimento, endereco)
        self.__tipo_habitacao = tipo_habitacao
        self.__possui_animais = possui_animais

    @property
    def tipo_habitacao(self):
        return self.__tipo_habitacao

    @tipo_habitacao.setter
    def tipo_habitacao(self, tipo_habitacao):
        if isinstance(tipo_habitacao, str):
            self.__tipo_habitacao = tipo_habitacao

    @property
    def possui_animais(self):
        return self.__possui_animais

    @possui_animais.setter
    def possui_animais(self, possui_animais):
        if isinstance(possui_animais, bool):
            self.__possui_animais = possui_animais