from persistence.DAO import DAO
from model.paciente import Paciente

class PacienteDAO(DAO):

    def __init__(self):
        super().__init__("paciente.pkl")

    def add(self, paciente):
        if (paciente is not None) and (isinstance(paciente, Paciente)):
            super().add(paciente.cpf, paciente)
