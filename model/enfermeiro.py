from model.pessoa import Pessoa
from model.paciente import Paciente

class Enfermeiro(Pessoa):
    def __init__(self, nome: str, cpf: int):
        if isinstance(nome, str) and isinstance(cpf, int): 
            super().__init__(nome, cpf)
        self.__pacientes = []

    @property
    def pacientes(self) -> list:
        return self.__pacientes

    def inclui_paciente(self, paciente: Paciente):
        if isinstance(paciente, Paciente):
            i = 0
            duplicado = False
            while i < len(self.__pacientes) and duplicado is False:
                if self.__pacientes[i].nome == paciente.nome:
                    duplicado == True
                i += 1
            if duplicado is not True:
                self.__pacientes.append(paciente)

    def altera_dados_enfermeiro(self):
        pass