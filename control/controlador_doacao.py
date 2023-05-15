from view.tela_doacao import TelaDoacao
from control.controlador_doador import ControladorDoador
from control.controlador_cachorro import ControladorCachorro
from control.controlador_gato import ControladorGato
from model.registro_doacao import RegistroDoacao

class ControladorDoacao():

    def __init__(self, controlador_ong):
        self.__doacoes = []
        self.__controlador_ong = controlador_ong
        self.__controlador_doador = ControladorDoador(self)
        self.__controlador_cachorro = ControladorCachorro(self)
        self.__controlador_gato = ControladorGato(self)
        self.__tela_doacao = TelaDoacao()



    #consulta de doacoes

    def mostra_doacoes(self):
        for doacao in self.__doacoes:
            self.__tela_doacao.mostra_doacoes(doacao) #serao objetos que passarao por aqui, ai vai ter que incluir seus atributos no print

    def mostra_doacoes_periodo(self):
        pass

    def voltar(self):
        self.__controlador_ong.mostra_tela()

    def mostra_tela_consulta(self):
        lista_opcoes = {1:self.mostra_doacoes, 2: self.mostra_doacoes_periodo, 3: self.voltar}

        opcao_escolhida = self.__tela_doacao.tela_opcoes_consulta()
        funcao_escolhida = lista_opcoes[opcao_escolhida]
        funcao_escolhida()

  
    #doacoes

    def mostra_tela_doacao(self):
        lista_opcoes = {1:self.doar, 2: self.cadastra_doador, 3: self.voltar}

        opcao_escolhida = self.__tela_doacao.tela_opcoes_doacao()
        funcao_escolhida = lista_opcoes[opcao_escolhida]
        funcao_escolhida()

    def cadastra_doador(self):
        self.__controlador_doador.cadastrar_doador()

        # averiguar se o doador nao é também um adotante, só pode ser um ou outro

    def doar(self):
        cpf = self.__tela_doacao.pedir_cpf()
        if cpf == 1:
            self.mostra_tela_doacao()

        else:
            lista_doadores_cadastrados = self.__controlador_doador.pegar_doadores()

            if cpf not in lista_doadores_cadastrados:
                opcao = self.__tela_doacao.cpf_nao_cadastrado()

                if opcao == 1:
                    self.cadastra_doador()
                    self.doar()

                elif opcao == 2:
                    self.mostra_tela_doacao()
    
        if cpf in lista_doadores_cadastrados:
            print('Cadastro de doador encontrado, iniciando doação!')
            opcao_escolhida = self.__tela_doacao.gato_ou_cachorro()

            if opcao_escolhida == 1:
                self.doar_gato(cpf)

            elif opcao_escolhida == 2:
                self.doar_cachorro(cpf)

            elif opcao_escolhida == 3:
                self.mostra_tela_doacao()

    def doar_cachorro(self, cpf):
        doacao = self.__controlador_cachorro.cadastra_cachorro()

        if doacao == 1:
            self.mostra_tela_doacao()

        elif isinstance(doacao, object):
            dados_finais = self.__tela_doacao.finalizar_doacao()
            doador = self.__controlador_doador.pegar_doador_cpf(cpf)
            nova_doacao = RegistroDoacao(dados_finais[0], doacao, doador, dados_finais[1])
            self.__doacoes.append(nova_doacao)
            self.__tela_doacao.sucesso_doacao('Cachorro')
        

    def doar_gato(self, cpf):
        doacao = self.__controlador_gato.cadastra_gato()
        if doacao == 1:
            self.mostra_tela_doacao()

        elif isinstance(doacao, object):
            dados_finais = self.__tela_doacao.finalizar_doacao()
            doador = self.__controlador_doador.pegar_doador_cpf(cpf)
            nova_doacao = RegistroDoacao(dados_finais[0], doacao, doador, dados_finais[1])
            self.__doacoes.append(nova_doacao)
            self.__tela_doacao.sucesso_doacao_gato()


    def listar_doadores(self):
        self.__controlador_doador.listar_doadores()

    def pegar_doadores(self):
        self.pegar_doadores()
    
    def listar_animais(self):
        cachorros = self.__controlador_cachorro.listar_cachorros()
        gatos = self.__controlador_gato.listar_gatos()
        
        return [cachorros, gatos]
