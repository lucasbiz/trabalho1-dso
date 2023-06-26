from view.tela_doacao import TelaDoacao
from control.controlador_doador import ControladorDoador
from control.controlador_cachorro import ControladorCachorro
from control.controlador_gato import ControladorGato
from model.registro_doacao import RegistroDoacao
from datetime import date
from model.gato import Gato
from model.doador import Doador


class ControladorDoacao():

    def __init__(self, controlador_ong):
        self.__doacoes = [RegistroDoacao('22/6/2023', Gato(123, 'Gato Doado', 'Siamês', []), Doador(99999999999, 'Lucas Doador 3', '02/05/00', 'Avenida Beira Mar'), 'Mudança de país')]
        self.__controlador_ong = controlador_ong
        self.__controlador_doador = ControladorDoador(self)
        self.__controlador_cachorro = ControladorCachorro(self)
        self.__controlador_gato = ControladorGato(self)
        self.__tela_doacao = TelaDoacao()

    # ========== SISTEMA DE DOAÇÃO ==========

    # TELA DE DOAÇÃO

    def mostra_tela_doacao(self):
        lista_opcoes = {1:self.doar, 2: self.listar_doacoes, 3: self.cadastra_doador, 4: self.editar_doador, 5: self.excluir_doador, 6: self.listar_doadores, 7: self.voltar}

        opcao_escolhida = self.__tela_doacao.tela_opcoes_doacao()
        funcao_escolhida = lista_opcoes[opcao_escolhida]
        funcao_escolhida()

    def cadastra_doador(self):
        self.__controlador_doador.cadastrar_doador()

    def editar_doador(self):
        opcao_escolhida = self.__controlador_doador.editar_doador()
        if opcao_escolhida == 1 or opcao_escolhida == 0 :
            self.mostra_tela_doacao()

    def excluir_doador(self):
        opcao_escolhida = self.__controlador_doador.remover_doador()
        if opcao_escolhida == 1 or opcao_escolhida == 0 :
            self.mostra_tela_doacao()

    def listar_doadores(self):
        opcao = self.__controlador_doador.listar_doadores()
        if opcao == 1:
            self.mostra_tela_doacao()

    def listar_doacoes(self):
        if self.__doacoes == []:
            self.__tela_doacao.sem_registro_doacoes()
            self.mostra_tela_doacao()
        else:
            lista_doacoes = []
            for doacao in self.__doacoes:
                lista_doacoes.append(doacao)
            opcao_escolhida = self.__tela_doacao.mostra_doacoes(lista_doacoes)
            if opcao_escolhida == 1:
                self.mostra_tela_doacao()

    def voltar(self):
        self.__controlador_ong.mostra_tela()

    # INICIANDO DOAÇÃO

    def doar(self):

        cpf = self.__tela_doacao.informe_cpf()

        if cpf == 1:
            self.mostra_tela_doacao()

        else:
            lista_doadores_cadastrados = self.__controlador_doador.pegar_doadores()

            if cpf not in lista_doadores_cadastrados:
                opcao = self.__tela_doacao.cpf_nao_cadastrado(cpf)

                if opcao == 2:
                    self.cadastra_doador()
                    self.doar()

                elif opcao == 1:
                    self.mostra_tela_doacao()
    
            elif cpf in lista_doadores_cadastrados:
                self.__tela_doacao.iniciando_doacao()
                opcao_escolhida = self.__tela_doacao.gato_ou_cachorro()

                if opcao_escolhida == 1:
                    self.doar()

                elif opcao_escolhida == 2:
                    self.doar_gato(cpf)

                elif opcao_escolhida == 3:
                    self.doar_cachorro(cpf)

    def doar_cachorro(self, cpf):
        data = date.today()
        data_doacao = '{}/{}/{}'.format(data.day, data.month, data.year)

        novo_cachorro = self.__controlador_cachorro.cadastra_cachorro()
        cpf_doador = cpf

        if novo_cachorro == 1:
            self.mostra_tela_doacao()
        
        if novo_cachorro == 2:
            self.doar_cachorro(cpf_doador)

        elif isinstance(novo_cachorro, object):
            doador = self.__controlador_doador.pegar_doador_cpf(cpf_doador)
            motivo = self.__tela_doacao.pedir_motivo()
            nova_doacao = RegistroDoacao(data_doacao, novo_cachorro, doador, motivo)
            self.__doacoes.append(nova_doacao)
            self.__tela_doacao.sucesso_doacao(novo_cachorro)
            self.mostra_tela_doacao() 

    def doar_gato(self, cpf):
        data = date.today()
        data_doacao = '{}/{}/{}'.format(data.day, data.month, data.year)

        novo_gato = self.__controlador_gato.cadastra_gato()
        cpf_doador = cpf

        if novo_gato == 1:
            self.mostra_tela_doacao()
        
        if novo_gato == 2:
            self.doar_gato(cpf_doador)

        elif isinstance(novo_gato, object):
            doador = self.__controlador_doador.pegar_doador_cpf(cpf_doador)
            motivo = self.__tela_doacao.pedir_motivo()
            nova_doacao = RegistroDoacao(data_doacao, novo_gato, doador, motivo)
            self.__doacoes.append(nova_doacao)
            self.__tela_doacao.sucesso_doacao(novo_gato)
            self.mostra_tela_doacao()

    def pegar_doadores(self):
        chaves_doadores = self.__controlador_doador.pegar_doadores()
        return chaves_doadores

    def listar_animais(self, opcao):
        if opcao == 3:
            self.__controlador_cachorro.listar_cachorros()
        if opcao == 2:
            self.__controlador_gato.listar_gatos()

    def voltar(self):
        self.__controlador_ong.mostra_tela()

    def verificar_adotantes(self):
        lista_cpfs_adotantes = self.__controlador_ong.verificar_adotantes()
        return lista_cpfs_adotantes


