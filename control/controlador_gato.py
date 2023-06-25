from view.tela_gato import TelaGato
from model.gato import Gato
from control.controlador_vacina import ControladorVacina
from datetime import date


class ControladorGato():

    def __init__(self, controlador_doacao):
        self.__gatos = {111: Gato(111, 'Thomas', 'Frajola', [])}
        self.__controlador_doacao = controlador_doacao
        self.__controlador_vacina = ControladorVacina()
        self.__tela_gato = TelaGato()

    def cadastra_gato(self):
        opcao_escolhida = self.__tela_gato.mostra_tela_cadastro()

        if opcao_escolhida == 1:
            return 1

        elif isinstance(opcao_escolhida, list):
            historico_vacinacao = []

            for item in opcao_escolhida:
                if isinstance(item, list):
                    historico_vacinacao.append(self.__controlador_vacina.cadastra_vacina(item[0], item[1]))

            if opcao_escolhida[0] not in self.__gatos:
                novo_gato = Gato(opcao_escolhida[0], opcao_escolhida[1], opcao_escolhida[2], historico_vacinacao)
                self.__gatos[opcao_escolhida[0]] = novo_gato
                self.__tela_gato.sucesso_cadastro_gato()

                return novo_gato

            elif opcao_escolhida[0] in self.__gatos:
                self.__tela_gato.gato_ja_cadastrado(opcao_escolhida[0])

        
    def listar_gatos(self):
        pass

    def finalizar_adocao(self, identificador):
        self.__gatos.pop(identificador)
    
    def verificar_vacinas(self, numero_chip):

        if len(self.__gatos[numero_chip].historico_vacinacao) == 3:
            return 2
        elif len(self.__gatos[numero_chip].historico_vacinacao) != 3:
            return 1
    
    def vacinar_gato_completo(self, gato, data_atual):

        lista_nomes_vacinas_gato = []
        lista_nomes_vacinas_completa = ['Raiva', 'Leptospirose', 'Hepatite infecciosa',]

        for vacina in gato.historico_vacinacao:
            lista_nomes_vacinas_gato.append(vacina.nome_vacina) #lista com os nomes das vacinas que o gato JÁ POSSUI

        for vac in lista_nomes_vacinas_completa:
            if vac not in lista_nomes_vacinas_gato:
                self.__controlador_vacina.vacinar(vac, data_atual)
                gato.historico_vacinacao.append(vac)

    def listar_gatos(self):

        if self.__gatos == {}:
            self.__tela_gato.sem_gatos()

        else:
            for gato_chave in self.__gatos:
                gato = self.__gatos[gato_chave]
                gato_infos = {'numero_chip': gato.numero_chip, 'nome': gato.nome, 'raca': gato.raca, 'tamanho': gato.tamanho}
                self.__tela_gato.mostra_gatos(gato_infos)

    def pegar_gato_pelo_numero(self):

        numero_chip = self.__tela_gato.pegar_gato_pelo_numero()

        if numero_chip in self.__gatos:
            return self.__gatos[numero_chip]

        elif numero_chip == 1:
            return 1

        elif numero_chip not in self.__gatos:
            self.__tela_gato.gato_nao_encontrado()
            return 1
