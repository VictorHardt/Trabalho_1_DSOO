from control.controladorVacina import ControladorVacina
from control.controladorAgendamento import ControladorAgendamento
from control.controladorPaciente import ControladorPaciente
from control.controladorEnfermeiro import ControladorEnfermeiro
from view.telaSistema import TelaSistema

class ControladorSistema:
    def __init__(self):
        self.__controlador_agendamento = ControladorAgendamento()
        self.__controlador_enfermeiro = ControladorEnfermeiro()
        self.__controlador_vacina = ControladorVacina()
        self.__controlador_paciente = ControladorPaciente()
        self.__tela = TelaSistema()
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
        self.__controlador_paciente.abre_tela()

    def abre_tela_agendamentos(self):
        self.__controlador_agendamento.abre_tela()

    def abre_tela_enfermeiros(self):
        self.__controlador_enfermeiro.abre_tela()

    def abre_tela_vacinas(self):
        self.__controlador_vacina.abre_tela()

    def sair(self):
        self.__continuar = False