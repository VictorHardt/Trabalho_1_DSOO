from model.paciente import Paciente
from view.telaPaciente import TelaPaciente

class ControladorPaciente:
    def __init__(self):
        self.__pacientes = []
        self.__tela = TelaPaciente()
        self.__continuar = True

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_paciente, 2: self.altera_dados_paciente(), 3: self.altera_dados_paciente(), 0: self.retorna}

        while self.__continuar:
            opcao_escolhida = self.__tela.mostrar_menu()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def cadastra_paciente(self):
        dados_paciente = self.__tela.recebe_dados_paciente()

        paciente = Paciente(dados_paciente["idade"], dados_paciente["nome"], dados_paciente["CPF"])

        duplicado = False
        for i in self.__pacientes:
            if i.cpf == paciente.cpf:
                self.__tela.cpf_duplicado_error(paciente.cpf)
                duplicado = True
        if not duplicado:
            self.__pacientes.append(paciente)

    def altera_dados_paciente(self):
        pass

    def exclui_paciente(self):
        pass

    def retorna_paciente(self, cpf:str) -> Paciente:
        pac = None
        for paciente in self.__pacientes:
            if paciente.cpf == cpf:
                pac = paciente
        return pac

    def retorna(self):
        self.__continuar = False