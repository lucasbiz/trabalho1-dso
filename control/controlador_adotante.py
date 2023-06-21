from view.tela_adotante import TelaAdotante
from model.adotante import Adotante

class ControladorAdotante():

    def __init__(self, controlador_adocao):
        self.__adotantes = {114: Adotante(114, 'Lucas adotante', '02/05/00', 'Rua Antonio Costa', ['casa', 'media']), 999: Adotante(999, 'Lucas adotante', '02/05/00', 'Rua Antonio Costa', ['apartamento', 'pequeno'])}
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

            for adotante_chave in self.__adotantes:
                adotante = self.__adotantes[adotante_chave]
                adotante_infos = {'nome': adotante.nome, 'cpf': adotante.cpf, 'data de nascimento': adotante.data_nascimento, 'endereço': adotante.endereco, 'tipo de habitacao': adotante.tipo_habitacao}
                self.__tela_adotante.mostra_adotantes(adotante_infos)

    def pegar_adotantes(self):
        chaves_adotantes = []

        for adotante_chave in self.__adotantes:
            chaves_adotantes.append(adotante_chave)
        print(chaves_adotantes)

        return chaves_adotantes
    
    def pegar_adotante_cpf(self, cpf):
        if cpf in self.__adotantes:
            return self.__adotantes[cpf]

        else:
            self.__tela_adotante.cpf_nao_encontrado()
