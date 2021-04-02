from control.controladorVacina import ControladorVacina
from control.controladorAgendamento import ControladorAgendamento
from control.controladorPaciente import ControladorPaciente
from control.controladorEnfermeiro import ControladorEnfermeiro
from view.telaSistema import TelaSistema

class ControladorSistema:
    def __init__(self):
        self.__controlador_agendamento = ControladorAgendamento(self)
        self.__controlador_enfermeiro = ControladorEnfermeiro(self)
        self.__controlador_vacina = ControladorVacina(self)
        self.__controlador_paciente = ControladorPaciente(self)
        self.__tela = TelaSistema(self)
        self.__continuar = True

    def abre_tela(self):

        lista_opcoes = {
            1: self.abre_tela_pacientes,
            2: self.abre_tela_enfermeiros,
            3: self.abre_tela_vacinas,
            4: self.abre_tela_agendamentos,
            0: self.sair
        }

        while self.__continuar:
            opcao_escolhida = self.__tela.mostrar_menu()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def abre_tela_pacientes(self):
        pass

    def abre_tela_agendamentos(self):
        pass

    def abre_tela_enfermeiros(self):
        pass

    def abre_tela_vacinas(self):
        pass

    def sair(self):
        self.__continuar = False