from view.tela_adocao import TelaAdocao
from control.controlador_adotante import ControladorAdotante
from control.controlador_cachorro import ControladorCachorro
from control.controlador_gato import ControladorGato
from model.registro_adocao import RegistroAdocao

class ControladorAdocao():

    def __init__(self, controlador_ong):
        self.__adocoes = []
        self.__controlador_ong = controlador_ong
        self.__controlador_adotante = ControladorAdotante(self)
        self.__controlador_cachorro = ControladorCachorro(self)
        self.__controlador_gato = ControladorGato(self)
        self.__tela_adocao = TelaAdocao()




    def mostra_adocoes(self):
        for adocao in self.__adocoes:
            self.__tela_adocao.mostra_adocoes(adocao) #serao objetos que passarao por aqui, ai vai ter que incluir seus atributos no print

    def mostra_adocoes_periodo(self):
        pass

    def voltar(self):
        self.__controlador_ong.mostra_tela()

    def mostra_tela_consulta(self):
        lista_opcoes = {1:self.mostra_adocoes, 2: self.mostra_adocoes_periodo, 3: self.voltar}

        opcao_escolhida = self.__tela_adocao.tela_opcoes_consulta()
        funcao_escolhida = lista_opcoes[opcao_escolhida]
        funcao_escolhida()

  
    #adocoes

    def mostra_tela_adocao(self):
        lista_opcoes = {1:self.adotar, 2: self.cadastra_adotante, 3: self.voltar}

        opcao_escolhida = self.__tela_adocao.tela_opcoes_adocao()
        funcao_escolhida = lista_opcoes[opcao_escolhida]
        funcao_escolhida()

    def cadastra_adotante(self):
        self.__controlador_adotante.cadastrar_adotante()

        # averiguar se o adotante nao é também um adotante, só pode ser um ou outro

    def adotar(self):
        cpf = self.__tela_adocao.pedir_cpf()
        if cpf == 1:
            self.mostra_tela_adocao()

        else:
            lista_adotantes_cadastrados = self.__controlador_adotante.pegar_adotantees()
            if cpf not in lista_adotantes_cadastrados:
                opcao = self.__tela_adocao.cpf_nao_cadastrado()
                if opcao == 1:
                    self.cadastra_adotante()
                    self.adotar()
                elif opcao == 2:
                    self.mostra_tela_adocao()
    
        if cpf in lista_adotantes_cadastrados:
            print('Cadastro de adotante encontrado, iniciando doação!')
            opcao_escolhida = self.__tela_adocao.gato_ou_cachorro()
            if opcao_escolhida == 1:
                self.adotar_gato(cpf)
            elif opcao_escolhida == 2:
                self.adotar_cachorro(cpf)
            elif opcao_escolhida == 3:
                self.mostra_tela_adocao()

    def adotar_cachorro(self, cpf):
        adocao = self.__controlador_cachorro.cadastra_cachorro()
        if adocao == 1:
            self.mostra_tela_adocao()
        elif isinstance(adocao, object):
            dados_finais = self.__tela_adocao.finalizar_adocao()
            adotante = self.__controlador_adotante.pegar_adotante_cpf(cpf)
            nova_adocao = RegistroAdocao(dados_finais[0], adocao, adotante, dados_finais[1])
            if nova_adocao.assinou_termo == 2:
                self.__tela_adocao.adocao_cancelada_termo()
                self.__controlador_ong.adotar()
            elif nova_adocao.assinou_termo == 1:
                self.__adocoes.append(nova_adocao)
                self.__tela_adocao.sucesso_adocao('Cachorro')
                self.__controlador_cachorro.finalizar_adocao(adocao.numero_chip)
        

    def adotar_gato(self, cpf):
        adocao = self.__controlador_gato.cadastra_gato()
        if adocao == 1:
            self.mostra_tela_adocao()
        elif isinstance(adocao, object):
            dados_finais = self.__tela_adocao.finalizar_adocao()
            adotante = self.__controlador_adotante.pegar_adotante_cpf(cpf)
            verificar_vacinas = self.__controlador_gato.verificar_vacinas()
            if verificar_vacinas == 2:
                nova_adocao = RegistroAdocao(dados_finais[0], adocao, adotante, dados_finais[1])
                if nova_adocao.assinou_termo == 2:
                    self.__tela_adocao.adocao_cancelada_termo()
                    self.__controlador_ong.adotar()
                elif nova_adocao.assinou_termo == 1:
                    self.__adocoes.append(nova_adocao)
                    self.__tela_adocao.sucesso_adocao('Gato')
                    self.__controlador_gato.finalizar_adocao(adocao.numero_chip)
            elif verificar_vacinas == 1:
                falta_vacinas = self.__tela_adocao.erro_falta_vacinas()
                if falta_vacinas == 1:
                    self.__controlador_gato.vacinar_gato_completo(adocao, dados_finais[0])
                    nova_adocao = RegistroAdocao(dados_finais[0], adocao, adotante, dados_finais[1])
                    if nova_adocao.assinou_termo == 2:
                        self.__tela_adocao.adocao_cancelada_termo()
                        self.__controlador_ong.adotar()
                    elif nova_adocao.assinou_termo == 1:
                        self.__adocoes.append(nova_adocao)
                        self.__tela_adocao.sucesso_adocao('Gato')
                        self.__controlador_gato.finalizar_adocao(adocao.numero_chip)
                elif falta_vacinas == 2:
                    self.__tela_adocao.cancelar_adocao_falta_vacinas()
                    self.mostra_tela_adocao()                  


    def listar_adotantes(self):
        self.__controlador_adotante.listar_adotantes()
