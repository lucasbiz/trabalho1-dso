from view.tela_cachorro import TelaCachorro
from model.cachorro import Cachorro
from control.controlador_vacina import ControladorVacina
from model.vacina import Vacina



class ControladorCachorro():

    def __init__(self, controlador_doacao):
        self.__cachorros = {111: Cachorro(111, 'Cachorro médio', 'Sem raça', [Vacina('Raiva', '12/5/2022')], 2), 222: Cachorro(222, 'Cachorro grande', 'Sem raça', [], 3)}
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

    def verificar_vacinas(self, numero_chip):

        if len(self.__cachorros[numero_chip].historico_vacinacao) == 3:
            return 2
        elif len(self.__cachorros[numero_chip].historico_vacinacao) != 3:
            return 1

    def listar_cachorros(self):
        if self.__cachorros == {}:
            self.__tela_cachorro.sem_cachorros()

        else:
            for cachorro_chave in self.__cachorros:
                cachorro = self.__cachorros[cachorro_chave]
                cachorro_infos = {'numero_chip': cachorro.numero_chip, 'nome': cachorro.nome, 'raca': cachorro.raca, 'tamanho': cachorro.tamanho}
                self.__tela_cachorro.mostra_cachorros(cachorro_infos)

    def finalizar_adocao(self, identificador):
        self.__cachorros.pop(identificador)

    def vacinar_cachorro_completo(self, cachorro, data_atual):

        lista_nomes_vacinas_cachorro = []
        lista_nomes_vacinas_completa = ['Raiva', 'Leptospirose', 'Hepatite infecciosa',]

        for vacina in cachorro.historico_vacinacao:
            lista_nomes_vacinas_cachorro.append(vacina.nome_vacina) #lista com os nomes das vacinas que o cachorro JÁ POSSUI

        for vac in lista_nomes_vacinas_completa:
            if vac not in lista_nomes_vacinas_cachorro:
                self.__controlador_vacina.vacinar(vac, data_atual)
                cachorro.historico_vacinacao.append(vac)

    
    def pegar_cachorro_pelo_numero(self):

        numero_chip = self.__tela_cachorro.pegar_cachorro_pelo_numero()

        if numero_chip in self.__cachorros:
            return self.__cachorros[numero_chip]

        elif numero_chip == 1:
            return 1

        elif numero_chip not in self.__cachorros:
            self.__tela_cachorro.cachorro_nao_encontrado()
            return 1
    

        