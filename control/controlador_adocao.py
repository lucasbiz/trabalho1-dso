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
        if self.__adocoes == []:
            self.__tela_adocao.sem_registro_adocoes()
        else:
            for adocao in self.__adocoes:
                dados_adocao = {'data da adoção': adocao.data, 'numero do animal adotado': adocao.animal.numero_chip, 'nome do adotante': adocao.adotante.nome }
                self.__tela_adocao.mostra_adocoes(dados_adocao)

    def voltar(self):
        self.__controlador_ong.mostra_tela()

    def mostra_tela_consulta(self):
        lista_opcoes = {1:self.mostra_adocoes, 2: self.voltar}

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

    def adotar(self):
        cpf = self.__tela_adocao.pedir_cpf()
        if cpf == 1:
            self.mostra_tela_adocao()

        else:
            lista_adotantes_cadastrados = self.__controlador_adotante.pegar_adotantes()

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
        cachorro = self.__controlador_cachorro.pegar_cachorro_pelo_numero()
        tipo_habitacao = self.__controlador_adotante.pegar_adotante_cpf(cpf).tipo_habitacao
        if cachorro == 1:
            self.mostra_tela_adocao()

        if int(cachorro.tamanho) == 3:
            print('PEGOU O TAMANHO DO DOG')
            if tipo_habitacao[0] == 'apartamento' and tipo_habitacao[1] == 'pequeno':
                self.__tela_adocao.erro_tamanho_apartamento()
                self.mostra_tela_adocao()
        else:

            if isinstance(cachorro, object):
                dados_finais = self.__tela_adocao.finalizar_adocao()
                adotante = self.__controlador_adotante.pegar_adotante_cpf(cpf)
                verificar_vacinas = self.__controlador_cachorro.verificar_vacinas(cachorro.numero_chip)

                if verificar_vacinas == 2:
                    nova_adocao = RegistroAdocao(dados_finais[0], cachorro, adotante, dados_finais[1])

                    if nova_adocao.assinou_termo == 2:
                        self.__tela_adocao.adocao_cancelada_termo()
                        self.__controlador_ong.adotar()

                    elif nova_adocao.assinou_termo == 1:
                        self.__adocoes.append(nova_adocao)
                        self.__tela_adocao.sucesso_adocao('Cachorro')
                        self.__controlador_cachorro.finalizar_adocao(cachorro.numero_chip)

                elif verificar_vacinas == 1:
                    falta_vacinas = self.__tela_adocao.erro_falta_vacinas()

                    if falta_vacinas == 1:
                        self.__controlador_cachorro.vacinar_cachorro_completo(cachorro, dados_finais[0])
                        nova_adocao = RegistroAdocao(dados_finais[0], cachorro, adotante, dados_finais[1])

                        if nova_adocao.assinou_termo == 2:
                            self.__tela_adocao.adocao_cancelada_termo()
                            self.__controlador_ong.adotar()

                        elif nova_adocao.assinou_termo == 1:
                            self.__adocoes.append(nova_adocao)
                            self.__tela_adocao.sucesso_adocao('Cachorro')
                            self.__controlador_cachorro.finalizar_adocao(cachorro.numero_chip)

                    elif falta_vacinas == 2:
                        self.__tela_adocao.cancelar_adocao_falta_vacinas()
                        self.mostra_tela_adocao() 
        

    def adotar_gato(self, cpf):
        gato = self.__controlador_gato.pegar_gato_pelo_numero()

        if gato == 1:
            self.mostra_tela_adocao()
        else:
            if isinstance(gato, object):
                dados_finais = self.__tela_adocao.finalizar_adocao()
                adotante = self.__controlador_adotante.pegar_adotante_cpf(cpf)
                verificar_vacinas = self.__controlador_gato.verificar_vacinas(gato.numero_chip)

                if verificar_vacinas == 2:
                    nova_adocao = RegistroAdocao(dados_finais[0], gato, adotante, dados_finais[1])

                    if nova_adocao.assinou_termo == 2:
                        self.__tela_adocao.adocao_cancelada_termo()
                        self.__controlador_ong.adotar()

                    elif nova_adocao.assinou_termo == 1:
                        self.__adocoes.append(nova_adocao)
                        self.__tela_adocao.sucesso_adocao('gato')
                        self.__controlador_gato.finalizar_adocao(gato.numero_chip)

                elif verificar_vacinas == 1:
                    falta_vacinas = self.__tela_adocao.erro_falta_vacinas()

                    if falta_vacinas == 1:
                        self.__controlador_gato.vacinar_gato_completo(gato, dados_finais[0])
                        nova_adocao = RegistroAdocao(dados_finais[0], gato, adotante, dados_finais[1])

                        if nova_adocao.assinou_termo == 2:
                            self.__tela_adocao.adocao_cancelada_termo()
                            self.__controlador_ong.adotar()

                        elif nova_adocao.assinou_termo == 1:
                            self.__adocoes.append(nova_adocao)
                            self.__tela_adocao.sucesso_adocao('Gato')
                            self.__controlador_gato.finalizar_adocao(gato.numero_chip)

                    elif falta_vacinas == 2:
                        self.__tela_adocao.cancelar_adocao_falta_vacinas()
                        self.mostra_tela_adocao()                


    def listar_adotantes(self):
        self.__controlador_adotante.listar_adotantes()

    def verificar_doadores(self):
        doadores = self.__controlador_ong.pegar_doadores()
        return doadores