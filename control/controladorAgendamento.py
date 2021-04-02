from model.agendamento import Agendamento
from view.telaAgendamento import TelaAgendamento

class ControladorAgendamento:
    def __init__(self):
        self.__tela = TelaAgendamento()
        self.__continuar = True

    def abre_tela(self):

        self.__continuar = True
        lista_opcoes = {
            1: self.novo_agendamento, 
            2: self.checa_agendamento, 
            3: self.remove_agendamento, 
            4: self.altera_agendamento, 
            0: self.retorna
        }
        while self.__continuar:            
            opcao_escolhida = self.__tela.mostrar_menu()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def novo_agendamento(self):
        pass

    def checa_agendamento(self):
        pass

    def remove_agendamento(self):
        pass

    def altera_agendamento(self):
        pass

    def retorna(self):
        self.__continuar = False