from persistence.DAO import DAO
from model.localArmazenamento import LocalArmazenamento

class LocalArmazenamentoDAO(DAO):

    def __init__(self):
        super().__init__("localArmazenamento.pkl")

    def add(self, localArmazenamento):
        if (localArmazenamento is not None) and (isinstance(localArmazenamento, LocalArmazenamento)):
            super().add(localArmazenamento.local, localArmazenamento)