from view.tela_vacina import TelaVacina
from model.vacina import Vacina

class ControladorVacina():

    def __init__(self):
        self.__tela_vacina = TelaVacina()
    
    def mostra_tela_vacinacao(self):
        dados_vacina = self.__tela_vacina.mostra_tela_vacinacao()
        if dados_vacina == 1:
            return 1
        elif isinstance(dados_vacina, list):
            vacina = Vacina(dados_vacina[0], dados_vacina[1])
            return vacina
    
    def confirma_vacina(self):
        opcao = self.__tela_vacina.confirma_vacina()
        return opcao

    def vacinar(self, vacina, data_aplicacao):
        aplicacao_vacina = Vacina(vacina, data_aplicacao)
        return aplicacao_vacina