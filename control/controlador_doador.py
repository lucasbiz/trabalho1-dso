from view.tela_doador import TelaDoador
from model.doador import Doador

class ControladorDoador():

    def __init__(self, controlador_doacao):
        self.__doadores = {112: Doador(112, 'Lucas', '02/05/00', 'Rua Antonio Costa')}
        self.__controlador_doacao = controlador_doacao
        self.__tela_doador = TelaDoador()

    def cadastrar_doador(self):
        self.tela_cadastro()
    
    def cancelar_cadastro(self):
        self.__controlador_doacao.mostra_tela_doacao()

    def tela_cadastro(self):
        opcao_escolhida = self.__tela_doador.mostra_tela_cadastro()

        if opcao_escolhida == 1:
            self.cancelar_cadastro()

        elif isinstance(opcao_escolhida, list):
            doador = Doador(opcao_escolhida[0], opcao_escolhida[1], opcao_escolhida[2], opcao_escolhida[3])
            self.__doadores[opcao_escolhida[0]] = doador
            self.__tela_doador.mostra_sucesso_cadastro(opcao_escolhida[0])
            #print(self.__doadores)
    
    def listar_doadores(self):
        if self.__doadores == {}:
            self.__tela_doador.sem_doadores()
        else:
            for doador_chave in self.__doadores:
                doador = self.__doadores[doador_chave]
                doador_infos = {'nome': doador.nome, 'cpf': doador.cpf, 'data de nascimento': doador.data_nascimento, 'endereço': doador.endereco}
                self.__tela_doador.mostra_doadores(doador_infos)

    def pegar_doadores(self):
        chaves_doadores = []
        for doador_chave in self.__doadores:
            chaves_doadores.append(doador_chave)
        return chaves_doadores
