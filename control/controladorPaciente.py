from model.paciente import Paciente
from view.telaPaciente import TelaPaciente

class ControladorPaciente:
    def __init__(self, controlador_sistema: ControladorSistema):
        self.__controlador_sistema = controlador_sistema
        self.__pacientes = []
        self.__tela = TelaPaciente(self)

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_paciente, 2: self.altera_dados, 3: self.possui_agendamento, 4: self.lista_espera, 0: self.retorna}

        while True:
            opcao_escolhida = self.__tela.mostrar_menu()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def cadastra_paciente(self):
        pass

    def altera_dados(self):
        pass

    def possui_agendamento(self):
        pass

    def exclui_agendamento(self): #?
        pass

    def coloca_na_fila_de_espera(self): #?
        pass

    def lista_espera(self):
        pass

    def retorna(self):
        pass