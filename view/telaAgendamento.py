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
        print("5 : Vacina Primeira Dose")
        print("6 : Agenda segunda Dose")
        print("7 : Vacina Segunda Dose")
        print("8 : Lista Pacientes Que Tomaram Uma Dose")
        print("9 : Lista Pacientes Que Tomaram Duas Doses")
        print("10 : Lista Pacientes Na Fila de Espera")
        print("11 : Imprime Relatório")
        print("0 : Retornar")
        print("")

        return self.ler_numero([1,2,3,4,5,6,7,8,9,10,11,0])

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
        input("")

    def enfermeiro_nao_existe_error(self, nome):
        print("")
        print("Não existe nenhum enfermeiro cadastrado com o nome {}, realize o cadastro do enfermeiro antes do agendamento.".format(nome))
        input("")

    def sem_estoque_de_vacina_error(self):
        print("")
        print("Não há doses suficientes de vacina para o agendamento, o paciente foi movido para a fila de espera.")
        input("")

    def mostra_agendamento(self, paciente_nome, enfermeiro_nome, ano, mes, dia, fabricante):
        print("")
        print("{}, você tem um agendamento para o dia {}/{}/{} com o enfermeiro {}, para ser vacinado com a vacina {}!".format(paciente_nome, dia, mes, ano, enfermeiro_nome, fabricante))
        input("")

    def nao_ha_agendamento(self, cpf):
        print("")
        print("Não há nenhum agendamento com o cpf {}.".format(cpf))
        input("")

    def removeu_agendamento(self, cpf):

        if cpf:
            print(f"Não há nenhum agendamento com o cpf {cpf}")
        elif cpf is None:
            print("Seu agendamento foi removido com sucesso!")
        input("")

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
        input("")

    def mostrar_agendamentos(self, agendamentos):

        print("")
        print("----- Lista de Agendamentos -----")
        print("")
        if len(agendamentos) > 0:
            for agendamento in agendamentos:
                print(agendamento)
        else:
            print("Não há nenhum agendamento!")
        input("")

    def vacina_primeira_dose(self, nome, vacina):

        if nome:
            print(f"{nome} tomou a primeira dose da vacina {vacina}")
        else:
            print("O paciente já tomou a primeira dose!")
        input("")
        
    def agendamento_segunda_dose(self, erro, nome=None, dia=None, mes=None, ano=None, hora=None):

        print("")
        if erro == "nao_tomou_primeira_dose":
            print("O paciente precisa tomar a primeira dose antes de agendar a segunda!")
        elif erro == "ja_tomou_segunda_dose":
            print("O paciente já tomou a segunda dose!")
        elif erro == "ja_agendado":
            print("O paciente já agendou a segunda!")
        else:
            print(f"A segunda dose de {nome} está agendada para o dia {dia}/{mes}/{ano}, as {hora} horas!")
        input("")

    def data_invalida_error(self, dia, mes, ano):

        print("")
        print("Data Inválida!")
        print(f"Digite uma data a partir de {dia}/{mes}/{ano}!")
        print("")

    def vacinado_completamente(self, erro, nome=None, vacina=None):

        print("")
        if erro == "ja_vacinado":
            print("O paciente já foi vacinado com a segunda dose.")
        if erro == "sem_agendamento":
            print("O paciente não possui nenhum agendamento para tomar a segunda dose.")
        else:
            print(f"O paciente {nome} tomou a segunda dose da vacina {vacina}!")
        input("")

    def lista_pacientes(self, pacientes: list):

        print("")
        for paciente in pacientes:
            print(paciente)
            print("")
        input("")

    def relatorio(self, qtd_vacinas_aplicadas, vacinados_uma_dose, vacinados_duas_doses, pacientes_na_lista_de_espera, pacientes_com_agendamento):
        print("")
        print("----- Relatório do Sistema -----")
        print("")
        print(f"Quantidade total de vacinas aplicadas: {qtd_vacinas_aplicadas}")
        print(f"Quantidade de pessoas que tomaram apenas uma dose: {vacinados_uma_dose}")
        print(f"Quantidade de pessoas que tomaram as duas doses: {vacinados_duas_doses}")
        print(f"Quantidade de pessoas que esperam na fila de vacinação: {pacientes_na_lista_de_espera}")
        print(f"Quantidade de pessoas com vacinação agendada: {pacientes_com_agendamento}")
