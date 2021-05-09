from persistence.DAO import DAO
from model.agendamento import Agendamento
from model.paciente import Paciente

class AgendamentoDAO(DAO):

    def __init__(self):
        super().__init__("agendamento.pkl")

    def add(self, agendamento):
        if (agendamento is not None) and (isinstance(agendamento, Agendamento)):
            super().add(agendamento.paciente.cpf, agendamento)
