from model.agendamento import Agendamento

class Paciente(Pessoa):
    def __init__(self, idade: int, nome: str):
        super().__init__(nome)
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

    # Vacinação? implementar classe ou incluir atributo na classe agendamento?