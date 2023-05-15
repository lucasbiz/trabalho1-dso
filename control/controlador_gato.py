from view.tela_gato import TelaGato
from model.gato import Gato
from control.controlador_vacina import ControladorVacina


class ControladorGato():

    def __init__(self, controlador_doacao):
        self.__gatos = {}
        self.__controlador_doacao = controlador_doacao
        self.__controlador_vacina = ControladorVacina()
        self.__tela_gato = TelaGato()

    def cadastra_gato(self):
        opcao_escolhida = self.__tela_gato.mostra_tela_cadastro()
        if opcao_escolhida == 1:
            return 1
        elif isinstance(opcao_escolhida, list):
            if opcao_escolhida[0] not in self.__gatos:
                vacinas = self.vacinacao()
                novo_gato = Gato(opcao_escolhida[0], opcao_escolhida[1], opcao_escolhida[2], vacinas)
                self.__gatos[opcao_escolhida[0]] = novo_gato
                self.__tela_gato.sucesso_cadastro_gato()
                return novo_gato
            elif opcao_escolhida[0] in self.__gatos:
                self.__tela_gato.gato_ja_cadastrado(opcao_escolhida[0])

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
        
    def listar_gatos(self):
        pass

    def vacinar_gato(self):
        pass

    def finalizar_adocao(self, identificador):
        self.__gatos.pop(identificador)