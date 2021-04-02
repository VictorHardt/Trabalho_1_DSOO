from view.abstractTela import AbstractTela
from datetime import date

class TelaAgendamento(AbstractTela):

    def __init__(self):
        pass
        
    def mostrar_menu(self):

        print("")
        print("------------Menu de Agendamentos------------")
        print("")
        print("1 : Novo Agendamento")
        print("2 : Checa Agendamento")
        print("3 : Remove Agendamento")
        print("4 : Checa Agendamento")
        print("5 : Altera Agendamento")
        print("0 : Retornar")
        print("")

        return self.ler_numero([1,2,3,4,0])

    def recebe_dados_agendamento(self):
        cpf_paciente = self.ler_string("Digite seu cpf: ")
        nome_enfermeiro = self.ler_string("Digite o nome do enfermeiro: ")
        data = None
        while not isinstance(data, date):
            try:
                ano = self.ler_numero(None, "Para que ano é o agendamento: ")
                mes = self.ler_numero([1,2,3,4,5,6,7,8,9,10,11,12], "Para que mês é o agendamento: ")
                dia = self.ler_numero([i+1 for i in range(31)], "Para que dia é o agendamento: ")
                data = date(ano, mes, dia)
            except Exception:
                print("A data não é válida!")
        hora = self.ler_numero([8,9,10,11,12,13,14,15,16,17,18], "Escolha um horário entre 8 e 16 horas: ")
        dados_agendamento = {"cpf": cpf_paciente, "nome_enfermeiro": nome_enfermeiro, "data": data, "hora": hora}
        return dados_agendamento

    def paciente_nao_existe_error(self, cpf):
        print("")
        print("Não existe nenhum paciente cadastrado com o cpf {}, realize o cadastro do paciente antes do agendamento.".format(cpf))
        print("")

    def enfermeiro_nao_existe_error(self, nome):
        print("")
        print("Não existe nenhum enfermeiro cadastrado com o nome {}, realize o cadastro do enfermeiro antes do agendamento.".format(nome)) 
        print("")

    def sem_estoque_de_vacina_error(self):
        print("")
        print("Não há doses suficientes de vacina para o agendamento.")
        print("")