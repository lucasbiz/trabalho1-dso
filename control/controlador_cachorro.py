from view.tela_cachorro import TelaCachorro
from model.cachorro import Cachorro
from control.controlador_vacina import ControladorVacina


class ControladorCachorro():

    def __init__(self, controlador_doacao):
        self.__cachorros = {}
        self.__controlador_doacao = controlador_doacao
        self.__controlador_vacina = ControladorVacina()
        self.__tela_cachorro = TelaCachorro()

    def cadastra_cachorro(self):
        opcao_escolhida = self.__tela_cachorro.mostra_tela_cadastro()
        if opcao_escolhida == 1:
            return 1
        elif isinstance(opcao_escolhida, list):
            if opcao_escolhida[0] not in self.__cachorros:
                vacinas = self.vacinacao()
                novo_cachorro = Cachorro(opcao_escolhida[0], opcao_escolhida[1], opcao_escolhida[2], opcao_escolhida[3], vacinas)
                self.__cachorros[opcao_escolhida[0]] = novo_cachorro
                self.__tela_cachorro.sucesso_cadastro_cachorro()
                return novo_cachorro
            elif opcao_escolhida[0] in self.__cachorros:
                self.__tela_cachorro.cachorro_ja_cadastrado(opcao_escolhida[0])

    def vacinacao(self):
        lista_vacinas = []
        confirma_vacina = 1
        while confirma_vacina == 1:
            obj_vacina = self.__controlador_vacina.mostra_tela_vacinacao()
            if obj_vacina == 1:
                self.__controlador_doacao.mostra_tela_doacao()
            elif isinstance(obj_vacina, object):
                lista_vacinas.append(obj_vacina)
                confirma_vacina = self.__controlador_vacina.confirma_vacina()
        return lista_vacinas

        
    def listar_cachorros(self):
        pass

    def vacinar_cachorro(self):
        pass

    def finalizar_adocao(self, identificador):
        self.__cachorros.pop(identificador)


        