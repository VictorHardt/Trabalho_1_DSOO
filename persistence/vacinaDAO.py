from persistence.DAO import DAO
from model.vacina import Vacina

class VacinaDAO(DAO):

    def __init__(self):
        super().__init__("vacina.pkl")

    def add(self, vacina):
        if (vacina is not None) and (isinstance(vacina, Vacina)):
            super().add(vacina.fabricante, vacina)
