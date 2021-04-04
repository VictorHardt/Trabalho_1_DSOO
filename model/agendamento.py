from model.enfermeiro import Enfermeiro
from model.paciente import Paciente
from model.vacina import Vacina
from datetime import date

class Agendamento:
    def __init__(self, data: date, hora: int, enfermeiro: Enfermeiro, paciente: Paciente, vacina: Vacina):
        if isinstance(data, date):
            self.__data = data
        if isinstance(hora, int):
            self.__hora = hora
        if isinstance(enfermeiro, Enfermeiro):
            self.__enfermeiro = enfermeiro
        if isinstance(paciente, Paciente):
            self.__paciente = paciente
        if isinstance(vacina, Vacina):
            self.__vacina = vacina
        self.__vacinado_primeira_dose = False
        self.__vacinado_completamente = False
        self.__data_segunda_dose = None
        self.__hora_segunda_dose = None

    @property
    def data(self)  -> date:
        return self.__data

    @data.setter
    def data(self, data: date):
        if isinstance(data, date):
            self.__data = data

    @property
    def hora(self) -> int:
        return self.__hora

    @hora.setter
    def hora(self, hora: int):
        if isinstance(hora, int):
            self.__hora = hora

    @property
    def enfermeiro(self) -> Enfermeiro:
        return self.__enfermeiro

    @enfermeiro.setter
    def enfermeiro(self, enfermeiro: Enfermeiro):
        if isinstance(enfermeiro, Enfermeiro):
            self.__enfermeiro = enfermeiro

    @property
    def paciente(self) -> Paciente:
        return self.__paciente

    @paciente.setter
    def paciente(self, paciente: Paciente):
        self.__paciente = paciente

    @property
    def vacina(self) -> Vacina:
        return self.__vacina

    @vacina.setter
    def vacina(self, vacina: Vacina):
        if isinstance(vacina, Vacina):
            self.__vacina = vacina

    @property
    def vacinado_primeira_dose(self) -> bool:
        return self.__vacinado_primeira_dose

    @vacinado_primeira_dose.setter
    def vacinado_primeira_dose(self, vacinado: bool):
        if isinstance(vacinado, bool):
            self.__vacinado_primeira_dose = vacinado

    @property
    def vacinado_completamente(self) -> bool:
        return self.__vacinado_completamente

    @vacinado_completamente.setter
    def vacinado_completamente(self, vacinado: bool):
        if isinstance(vacinado, bool):
            self.__vacinado_completamente = vacinado

    @property
    def data_segunda_dose(self) -> date:
        return self.__data_segunda_dose

    @data_segunda_dose.setter
    def data_segunda_dose(self, data: date):
        if isinstance(data, date):
            self.__data_segunda_dose = data

    @property
    def hora_segunda_dose(self) -> int:
        return self.__hora_segunda_dose

    @hora_segunda_dose.setter
    def hora_segunda_dose(self, hora: int):
        if isinstance(hora, int):
            self.__hora_segunda_dose = hora
    