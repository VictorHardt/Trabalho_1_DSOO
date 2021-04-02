from model.paciente import Paciente
from view.telaPaciente import TelaPaciente
from control.controladorSistema import ControladorSistema

class ControladorPaciente:
    def __init__(self, controlador_sistema: ControladorSistema):
        self.__controlador_sistema = controlador_sistema
        self.__pacientes = []
        self.__tela = TelaPaciente(self)

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_paciente, 2: self.altera_dados_paciente(), 3: self.altera_dados_paciente(), 4: self.possui_agendamento, 5: self.lista_espera, 0: self.retorna}

        while True:
            opcao_escolhida = self.__tela.mostrar_menu()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def cadastra_paciente(self):
        dados_paciente = self.__tela.recebe_dados_paciente()

        paciente = Paciente(dados_paciente["idade"], dados_paciente["nome"], dados_paciente["CPF"])

        for i in self.__pacientes:
            if "CPF" == paciente.cpf:
                self.__tela.cpf_duplicado_error(paciente.cpf)
            else:
                self.__pacientes.append(paciente)

    def altera_dados_paciente(self):
        pass

    def exclui_paciente(self):
        pass

    def possui_agendamento(self):
        pass

    def lista_espera(self):
        pass

    def retorna(self):
        pass