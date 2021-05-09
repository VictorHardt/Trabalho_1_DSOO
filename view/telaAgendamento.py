from view.abstractTela import AbstractTela
from datetime import date
import PySimpleGUI as sg
from view.telaDadosAgendamento import TelaDadosAgendamento

class TelaAgendamento(AbstractTela):

    def __init__(self):
        self.__window = None
        self.init_components([])
        self.__tela_dados_agendamento = TelaDadosAgendamento()

    def init_components(self, agendamentos):
        layout = []
        for i in range(len(agendamentos)):
            linha = [sg.Radio("{} - {}".format(agendamentos[i][0], agendametos[i][1]), "agendamento", size=(10, 1))]
            layout.append(linha)
        layout.append([sg.Button("Novo", size=(7,0), key="1"), sg.Button("Alterar", size=(7,0), key="2"), sg.Button("Excluir", size=(7,0), key="3")])
        layout.append([sg.Button("Vacina", size=(7,0), key="4"), sg.Button("Vacinados", size=(7,0), key="5"), sg.Button("Lista de Espera", size=(7,0), key="6")])
        layout.append([sg.Text("", size=(7,0)),sg.Button("Relatório", key="7")])
        self.__window = sg.Window("Agendamento").Layout(layout)

    def mostrar_menu(self, agendamentos):
        self.init_components(agendamentos)
        botao, valores = self.__window.Read()
        if botao is None:
            botao = 0
        agendamento = None
        for i in range(len(valores.values())):
            if valores[i]:
                agendamento = agendamentos[i][1]
        self.close()
        return (int(botao), agendamento)

    def recebe_dados_agendamento(self):
        return self.__tela_dados_agendamento.recebe_dados()

    def paciente_nao_existe_error(self, cpf):
        msg = ("Não existe nenhum paciente cadastrado com o cpf {}, realize o cadastro do paciente antes do agendamento.".format(cpf))
        self.popup(msg)

    def enfermeiro_nao_existe_error(self, cpf):

        self.popup("Não existe nenhum enfermeiro cadastrado com o cpf {}, realize o cadastro do enfermeiro antes do agendamento.".format(cpf))

    def sem_estoque_de_vacina_error(self):
        self.popup("Não há doses suficientes de vacina para o agendamento, o paciente foi movido para a fila de espera.")

    def mostra_agendamento(self, paciente_nome, enfermeiro_nome, ano, mes, dia, fabricante):
        self.popup("{}, você tem um agendamento para o dia {}/{}/{} com o enfermeiro {}, para ser vacinado com a vacina {}!".format(paciente_nome, dia, mes, ano, enfermeiro_nome, fabricante))

    def nao_ha_agendamento(self, cpf):
        self.popup("Não há nenhum agendamento com o cpf {}.".format(cpf))

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

    def escolher_enfermeiro(self):
        return self.ler_string("Digite o nome do enfermeiro: ")

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

    def popup(self, msg):
        sg.Popup("", "{}".format(msg))

    def close(self):
        self.__window.Close()
