from view.tela_doador import TelaDoador
from model.doador import Doador

class ControladorDoador():

    def __init__(self, controlador_doacao):
        self.__doadores = {33333333333: Doador(33333333333, 'Lucas Doador', '02/05/00', 'Rua Sempre Viva')}
        self.__controlador_doacao = controlador_doacao
        self.__tela_doador = TelaDoador()

    def cadastrar_doador(self):
        opcao_escolhida = self.tela_cadastro()

        if opcao_escolhida == 1:
            self.cancelar_cadastro()

        elif isinstance(opcao_escolhida, list):
            if opcao_escolhida[0] not in self.__doadores:
                doador = Doador(opcao_escolhida[0], opcao_escolhida[1], opcao_escolhida[2], opcao_escolhida[3])
                self.__doadores[opcao_escolhida[0]] = doador
                self.__tela_doador.mostra_sucesso_cadastro(opcao_escolhida[0])
                self.__controlador_doacao.mostra_tela_doacao()

            elif opcao_escolhida[0] in self.__doadores:
                self.__tela_doador.cpf_ja_cadastrado(opcao_escolhida[0])
                self.__controlador_doacao.mostra_tela_doacao()

    
    def cancelar_cadastro(self):
        self.__controlador_doacao.mostra_tela_doacao()

    def tela_cadastro(self):
        opcao_escolhida = self.__tela_doador.mostra_tela_cadastro()
        return opcao_escolhida

    def listar_doadores(self):

        if self.__doadores == {}:
            self.__tela_doador.sem_doadores()
            return 1

        else:
            lista_doadores = []
            for doador_chave in self.__doadores:
                doador = self.__doadores[doador_chave]
                lista_doadores.append(doador)
            opcao_escolhida = self.__tela_doador.mostra_doadores(lista_doadores)
            if opcao_escolhida == 1:
                return 1

    def pegar_doadores(self):

        chaves_doadores = []

        for doador_chave in self.__doadores:
            chaves_doadores.append(doador_chave)
    
        return chaves_doadores
    
    def pegar_doador_cpf(self, cpf):
        if cpf in self.__doadores:
            return self.__doadores[cpf]
        else:
            self.__tela_doador.cpf_nao_encontrado()

    def editar_doador(self):

        cpf_informado = self.informe_cpf()

        if cpf_informado == 1:
            return 1

        elif cpf_informado in self.__doadores:
            doador_editado = self.__tela_doador.tela_edicao_doador(self.__doadores[cpf_informado])
            self.__doadores.pop(cpf_informado)

            if doador_editado == 1:
                return 1   

            elif doador_editado[0] not in self.__controlador_doacao.verificar_adotantes():
                doador = Doador(doador_editado[0], doador_editado[1], doador_editado[2], doador_editado[3])
                self.__doadores[cpf_informado] = doador
                self.__tela_doador.mostra_sucesso_edicao(doador_editado[0])
                return 0

            elif doador_editado[0] in self.__doadores:
                self.__tela_doador.cpf_ja_cadastrado(doador_editado[0])
                self.__controlador_doacao.mostra_tela_doacao()

            elif doador_editado[0] in self.__controlador_doacao.verificar_adotantes():
                self.__tela_doador.cpf_ja_cadastrado_doador(doador_editado[0])
                self.__controlador_doacao.mostra_tela_doacao()  
   
        else:
            self.__tela_doador.cpf_nao_encontrado(cpf_informado)
            return 1


    def informe_cpf(self):

        cpf_informado = self.__tela_doador.informe_cpf()

        return cpf_informado

    def remover_doador(self):

        cpf_informado = self.informe_cpf()

        if cpf_informado == 1:
            return 1

        elif cpf_informado in self.__doadores:
            self.__doadores.pop(cpf_informado)
            self.__tela_doador.doador_removido_sucesso(cpf_informado)
            return 0

        else:
            self.__tela_doador.cpf_nao_encontrado(cpf_informado)
            return 1
