class Agendamento:
    def __init__(self, data: date, hora: int, enfermeiro: Enfermeiro, paciente: Paciente, vacina: vacina):
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
    def paciente(self) -> paciente:
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

 