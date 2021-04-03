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
        print("4 : Altera Agendamento")
        print("0 : Retornar")
        print("")

        return self.ler_numero([1,2,3,4,0])

    def recebe_dados_agendamento(self):

        cpf_paciente = self.recebe_cpf()
        nome_enfermeiro = self.escolher_enfermeiro()
        data = self.escolher_data()
        hora = self.escolher_hora()
        dados_agendamento = {"cpf": cpf_paciente, "nome_enfermeiro": nome_enfermeiro, "data": data, "hora": hora}
        return dados_agendamento

    def recebe_cpf(self):
        return self.ler_string("Digite seu cpf: ")

    def paciente_nao_existe_error(self, cpf):
        print("")
        print("Não existe nenhum paciente cadastrado com o cpf {}, realize o cadastro do paciente antes do agendamento.".format(cpf))

    def enfermeiro_nao_existe_error(self, nome):
        print("")
        print("Não existe nenhum enfermeiro cadastrado com o nome {}, realize o cadastro do enfermeiro antes do agendamento.".format(nome)) 

    def sem_estoque_de_vacina_error(self):
        print("")
        print("Não há doses suficientes de vacina para o agendamento.")

    def mostra_agendamento(self, paciente_nome, enfermeiro_nome, ano, mes, dia, fabricante):
        print("")
        print("{}, você tem um agendamento para o dia {}/{}/{} com o enfermeiro {}, para ser vacinado com a vacina {}".format(paciente_nome, enfermeiro_nome, ano, mes, dia, fabricante))

    def nao_ha_agendamento(self, cpf):
        print("")
        print("Não há nenhum agendamento com o cpf {}.".format(cpf))

    def removeu_agendamento(self, cpf):

        if cpf:
            print(f"Não há nenhum agendamento com o cpf {cpf}")
        elif cpf is None:
            print("Seu agendamento foi removido com sucesso!")

    def opcao_para_alteracao(self):

        print("O que você quer alterar no agendamento?")
        print("")
        print("1 : Data")
        print("2 : Hora")
        print("3 : Enfermeiro")
        print("4 : Paciente")

        return self.ler_numero([1,2,3,4])

    def escolher_data(self):
        data = None
        while not isinstance(data, date):
            try:
                ano = self.ler_numero(None, "Para que ano é o agendamento: ")
                mes = self.ler_numero([1,2,3,4,5,6,7,8,9,10,11,12], "Para que mês é o agendamento: ")
                dia = self.ler_numero([i+1 for i in range(31)], "Para que dia é o agendamento: ")
                data = date(ano, mes, dia)
            except Exception:
                print("A data não é válida!")
        return data

    def escolher_enfermeiro(self):
        return self.ler_string("Digite o nome do enfermeiro: ")

    def escolher_hora(self):
        return self.ler_numero([8,9,10,11,12,13,14,15,16,17,18], "Escolha um horário entre 8 e 18 horas: ")
    
    def escolher_paciente(self):
        return self.ler_string("Digite o cpf do novo paciente: ")

    def alterado(self):
        print("")
        print("Seu agendamento foi alterado com sucesso!")