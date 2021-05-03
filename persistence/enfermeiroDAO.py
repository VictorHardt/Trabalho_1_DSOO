from persistence.DAO import DAO
from model.enfermeiro import Enfermeiro

class EnfermeiroDAO(DAO):

    def __init__(self):
        super().__init__("enfermeiro.pkl")

    def add(self, enfermeiro):
        if (enfermeiro is not None) and (isinstance(enfermeiro, Enfermeiro)):
            super().add(enfermeiro.cpf, enfermeiro)
