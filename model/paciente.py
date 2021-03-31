from model.agendamento import Agendamento
from model.pessoa import Pessoa

class Paciente(Pessoa):
    def __init__(self, idade: int, nome: str, cpf: int):
        if isinstance(nome, str) and isinstance(cpf, int):
            super().__init__(nome, cpf)
        if isinstance(idade, int):
            self.__idade = idade

    @property
    def idade(self) -> int:
        return self.__idade

    @idade.setter
    def idade(self, idade: int):
        if isinstance(idade, int):
            self.__idade = idade

    @property
    def agendamento(self) -> Agendamento:
        return self.__agendamento

    @agendamento.setter
    def agendamento(self, agendamento: Agendamento):
        if isinstance(agendamento, Agendamento):
            self.__agendamento = agendamento