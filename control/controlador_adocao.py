from view.tela_adocao import TelaAdocao
from control.controlador_adotante import ControladorAdotante
from control.controlador_cachorro import ControladorCachorro
from control.controlador_gato import ControladorGato
from model.registro_adocao import RegistroAdocao
from model.gato import Gato
from model.adotante import Adotante

class ControladorAdocao():

    def __init__(self, controlador_ong):
        self.__adocoes = [RegistroAdocao('22/6/2023', Gato(123, 'Thomas', 'Frajola', []), Adotante(11237723981, 'Lucas adotante 3', '02/05/00', 'Avenida Beira Mar', 'Casa média'), True) ]
        self.__controlador_ong = controlador_ong
        self.__controlador_adotante = ControladorAdotante(self)
        self.__controlador_cachorro = ControladorCachorro(self)
        self.__controlador_gato = ControladorGato(self)
        self.__tela_adocao = TelaAdocao()


    # ========== SISTEMA DE ADOÇÃO ==========
    # TELA DE ADOÇÃO
    def mostra_tela_adocao(self):
        lista_opcoes = {1:self.adotar, 2: self.listar_adocoes, 3: self.cadastra_adotante, 4: self.editar_adotante, 5: self.excluir_adotante, 6: self.listar_adotantes, 7: self.voltar}

        opcao_escolhida = self.__tela_adocao.tela_opcoes_adocao()
        funcao_escolhida = lista_opcoes[opcao_escolhida]
        funcao_escolhida()

    def cadastra_adotante(self):
        self.__controlador_adotante.cadastrar_adotante()

    def editar_adotante(self):
        opcao_escolhida = self.__controlador_adotante.editar_adotante()
        if opcao_escolhida == 1 or opcao_escolhida == 0 :
            self.mostra_tela_adocao()

    def excluir_adotante(self):
        opcao_escolhida = self.__controlador_adotante.remover_adotante()
        if opcao_escolhida == 1 or opcao_escolhida == 0 :
            self.mostra_tela_adocao()

    def listar_adotantes(self):
        opcao = self.__controlador_adotante.listar_adotantes()
        if opcao == 1:
            self.mostra_tela_adocao()

    def listar_adocoes(self):
        if self.__adocoes == []:
            self.__tela_adocao.sem_registro_adocoes()
        else:
            lista_adocoes = []
            for adocao in self.__adocoes:
                lista_adocoes.append(adocao)
            opcao_escolhida = self.__tela_adocao.mostra_adocoes(lista_adocoes)
            if opcao_escolhida == 1:
                self.mostra_tela_adocao()

    def voltar(self):
        self.__controlador_ong.mostra_tela()


    # INICIANDO ADOÇÃO

    def adotar(self):
        cpf = self.__controlador_adotante.informe_cpf()
        lista_cpfs_adotantes = self.__controlador_adotante.pegar_cpf_adotantes() # retorna os cpfs dos adotantes cadastrados

        if cpf == 1:
            self.mostra_tela_adocao()

        else:
            #verifica se o cpf esta ou nao na lista
            if cpf not in lista_cpfs_adotantes:
                opcao = self.__tela_adocao.cpf_nao_cadastrado(cpf) # se nao estivar, pergunta se quer cadastrar ou nao

                if opcao == 1:
                    self.mostra_tela_adocao()

                else:
                    self.cadastra_adotante()

        # se estiver, inicia a doação perguntando se o adotante quer adotar um gato ou cachorro
        if cpf in lista_cpfs_adotantes:
            self.__tela_adocao.iniciando_adocao()
            opcao_escolhida = self.__tela_adocao.gato_ou_cachorro()

            if opcao_escolhida == 1:
                self.mostra_tela_adocao()

            elif opcao_escolhida == 2:
                self.adotar_gato(cpf) # se for gato, vai para adocao de gatos

            elif opcao_escolhida == 3:
                self.adotar_cachorro(cpf) # se for cachorro, vai para adocao de cachorros


    def adotar_cachorro(self, cpf):

        cachorro = self.__controlador_cachorro.pegar_cachorro_pelo_numero()
        adotante = self.__controlador_adotante.pegar_adotante_cpf(cpf)

        if cachorro == 1:
            self.mostra_tela_adocao()

        if int(cachorro.tamanho) == 3:
            if adotante.tipo_habitacao == 'Apartamento pequeno':
                self.__tela_adocao.erro_tamanho_apartamento()
                self.mostra_tela_adocao()
        else:

            if isinstance(cachorro, object):
                dados_finais = self.__tela_adocao.finalizar_adocao()
                verificar_vacinas = self.__controlador_cachorro.verificar_vacinas(cachorro.numero_chip)

                if verificar_vacinas == 2:
                    nova_adocao = RegistroAdocao(dados_finais, cachorro, adotante, True)
                    self.__adocoes.append(nova_adocao)
                    self.__tela_adocao.sucesso_adocao('Cachorro')
                    self.__controlador_cachorro.finalizar_adocao(cachorro.numero_chip)

                elif verificar_vacinas == 1:
                    falta_vacinas = self.__tela_adocao.erro_falta_vacinas(cachorro.historico_vacinacao)

                    if falta_vacinas == 2:
                        self.__controlador_cachorro.vacinar_cachorro_completo(cachorro, dados_finais)
                        nova_adocao = RegistroAdocao(dados_finais, cachorro, adotante, True)
                        self.__adocoes.append(nova_adocao)
                        self.__tela_adocao.sucesso_adocao('Cachorro')
                        self.__controlador_cachorro.finalizar_adocao(cachorro.numero_chip)
                        self.__controlador_ong.mostra_tela()

                    elif falta_vacinas == 1:
                        self.mostra_tela_adocao() 
        

    def adotar_gato(self, cpf):
        adotante = self.__controlador_adotante.pegar_adotante_cpf(cpf)
        gato = self.__controlador_gato.pegar_gato_pelo_numero()

        if gato == 1:
            self.mostra_tela_adocao()
        else:
            if isinstance(gato, object):
                dados_finais = self.__tela_adocao.finalizar_adocao() #funcao que só retorna a data quando o usuario assina o termo, caso nao assine volta ao painel de adocao

                if dados_finais == 1:
                    self.mostra_tela_adocao()

                else:
                    verificar_vacinas = self.__controlador_gato.verificar_vacinas(gato.numero_chip)

                    if verificar_vacinas == 2:
                        nova_adocao = RegistroAdocao(dados_finais, gato, adotante, True)
                        self.__adocoes.append(nova_adocao)
                        self.__tela_adocao.sucesso_adocao('gato')
                        self.__controlador_gato.finalizar_adocao(gato.numero_chip)

                    elif verificar_vacinas == 1:
                        falta_vacinas = self.__tela_adocao.erro_falta_vacinas(gato.historico_vacinacao)

                        if falta_vacinas == 2:
                            self.__controlador_gato.vacinar_gato_completo(gato, dados_finais)
                            nova_adocao = RegistroAdocao(dados_finais, gato, adotante, True)
                            self.__adocoes.append(nova_adocao)
                            self.__tela_adocao.sucesso_adocao('Gato')
                            self.__controlador_gato.finalizar_adocao(gato.numero_chip)
                            self.__controlador_ong.mostra_tela()

                        elif falta_vacinas == 1:
                            self.mostra_tela_adocao()                

    def verificar_doadores(self):
        cpfs_doadores = self.__controlador_ong.pegar_doadores()
        return cpfs_doadores

    def mostra_tela_consulta(self):
        lista_opcoes = {1:self.mostra_adocoes, 2: self.voltar}

        opcao_escolhida = self.__tela_adocao.tela_opcoes_consulta()
        funcao_escolhida = lista_opcoes[opcao_escolhida]
        funcao_escolhida()

  

