from view.tela_adotante import TelaAdotante
from model.adotante import Adotante

class ControladorAdotante():

    def __init__(self, controlador_adocao):
        self.__adotantes = {11111111111: Adotante(11111111111, 'Lucas adotante', '02/05/2000', 'Rua Antonio Costa', 'Casa média'), 22222222222: Adotante(22222222222, 'Lucas adotante 2', '02/05/00', 'Avenida Madre Benvenuta', 'Apartamento pequeno')}
        self.__controlador_adocao = controlador_adocao
        self.__tela_adotante = TelaAdotante()

    def cadastrar_adotante(self):
        self.tela_cadastro()
    
    def cancelar_cadastro(self):
        self.__controlador_adocao.mostra_tela_adocao()

    def tela_cadastro(self):
        opcao_escolhida = self.__tela_adotante.mostra_tela_cadastro()

        if opcao_escolhida == 1:
            self.cancelar_cadastro()

        elif isinstance(opcao_escolhida, list):

            if opcao_escolhida[0] not in self.__adotantes and opcao_escolhida[0] not in self.__controlador_adocao.verificar_doadores():
                adotante = Adotante(opcao_escolhida[0], opcao_escolhida[1], opcao_escolhida[2], opcao_escolhida[3], opcao_escolhida[4])
                self.__adotantes[opcao_escolhida[0]] = adotante
                self.__tela_adotante.mostra_sucesso_cadastro(opcao_escolhida[0])

            elif opcao_escolhida[0] in self.__adotantes:
                self.__tela_adotante.cpf_ja_cadastrado(opcao_escolhida[0])
                self.__controlador_adocao.mostra_tela_adocao()

            elif opcao_escolhida[0] in self.__controlador_adocao.verificar_doadores():
                self.__tela_adotante.cpf_ja_cadastrado_doador(opcao_escolhida[0])
                self.__controlador_adocao.mostra_tela_adocao()               

    def listar_adotantes(self):

        if self.__adotantes == {}:
            self.__tela_adotante.sem_adotantes()

        else:
            lista_adotantes = []
            for adotante_chave in self.__adotantes:
                adotante = self.__adotantes[adotante_chave]
                lista_adotantes.append(adotante)
            opcao_escolhida = self.__tela_adotante.mostra_adotantes(lista_adotantes)
            if opcao_escolhida == 1:
                return 1


    def pegar_cpf_adotantes(self):
        chaves_adotantes = []

        for adotante_chave in self.__adotantes:
            chaves_adotantes.append(adotante_chave)

        return chaves_adotantes
    
    def pegar_adotante_cpf(self, cpf):
        if cpf in self.__adotantes:
            return self.__adotantes[cpf]

        else:
            self.__tela_adotante.cpf_nao_encontrado()

    def remover_adotante(self):

        cpf_informado = self.informe_cpf()

        if cpf_informado == 1:
            return 1

        elif cpf_informado in self.__adotantes:
            self.__adotantes.pop(cpf_informado)
            self.__tela_adotante.adotante_removido_sucesso(cpf_informado)
            return 0

        else:
            self.__tela_adotante.cpf_nao_encontrado(cpf_informado)
            return 1

    def editar_adotante(self):
        cpf_informado = self.informe_cpf()

        if cpf_informado == 1:
            return 1

        elif cpf_informado in self.__adotantes:
            adotante_editado = self.__tela_adotante.tela_edicao_adotante(self.__adotantes[cpf_informado])
            self.__adotantes.pop(cpf_informado)

            if adotante_editado == 1:
                return 1   

            elif adotante_editado[0] not in self.__controlador_adocao.verificar_doadores():
                adotante = Adotante(adotante_editado[0], adotante_editado[1], adotante_editado[2], adotante_editado[3], adotante_editado[4])
                self.__adotantes[cpf_informado] = adotante
                self.__tela_adotante.mostra_sucesso_edicao(adotante_editado[0])
                return 0

            elif adotante_editado[0] in self.__adotantes:
                self.__tela_adotante.cpf_ja_cadastrado(adotante_editado[0])
                self.__controlador_adocao.mostra_tela_adocao()

            elif adotante_editado[0] in self.__controlador_adocao.verificar_doadores():
                self.__tela_adotante.cpf_ja_cadastrado_doador(adotante_editado[0])
                self.__controlador_adocao.mostra_tela_adocao()  
   
        else:
            self.__tela_adotante.cpf_nao_encontrado(cpf_informado)
            return 1


    def informe_cpf(self):

        cpf_informado = self.__tela_adotante.informe_cpf()

        return cpf_informado

    def verificar_adotantes(self):
        lista_adotantes = []
        for adotante_chave in self.__adotantes:
            adotante = self.__adotantes[adotante_chave]
            lista_adotantes.append(adotante)
        return lista_adotantes




          
