from model.pessoa import Pessoa

class Enfermeiro(Pessoa):
    def __init__(self, nome: str, cpf: str):
        if isinstance(nome, str) and isinstance(cpf, str): 
            super().__init__(nome, cpf)
        self.__pacientes = []

    @property
    def pacientes(self) -> list:
        return self.__pacientes