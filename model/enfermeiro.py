from pessoa.py import Pessoa
from agendamento impot Agendamento
from paciente import Paciente

class Enfermeiro(Pessoa):
    def __init__(self, nome: str, cpf: int):
        if isinstance(nome, str) and isinstance(cpf, int): 
            super().__init__(nome, cpf)
        self.__agendamentos = []
        self.__pacientes = []

    @property
    def agendamentos(self) -> list:
        return self.__agendamentos

    @property
    def pacientes(self) -> list:
        return self.__pacientes

    def inclui_agendamento(self, agendamento: Agendamento):

        if isinstance(agendamento, Agendamento):
            i = 0
            duplicado = False
            while i < len(self.__agendamentos) and duplicado is False:
                if self.__agendamentos[i].hora == agendamento.hora:
                    duplidado == True
                i += 1
            if duplicado is not True:
                self.__agendamentos.append(agendamento)

    def inclui_paciente(self, paciente: Paciente):
        if isinstance(paciente, Paciente):
            i = 0
            duplicado = False
            while i < len(self.__pacientes) and duplicado is False:
                if self.__pacientes[i].nome == paciente.nome:
                    duplidado == True
                i += 1
            if duplicado is not True:
                self.__pacientes.append(paciente)

