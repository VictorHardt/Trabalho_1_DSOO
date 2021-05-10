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
            linha = [sg.Radio("{} - {} - {} - {} - {} - {}".format(agendamentos[i][0], agendamentos[i][1], agendamentos[i][2], agendamentos[i][3], agendamentos[i][4], agendamentos[i][5]), "agendamento")]
            layout.append(linha)
        layout.append([sg.Button("Novo", size=(7,0), key="1"), sg.Button("Alterar", size=(7,0), key="2"), sg.Button("Excluir", size=(7,0), key="3")])
        layout.append([sg.Button("Vacina", size=(7,0), key="4"), sg.Button("Lista de Espera", size=(7,0), key="5"), sg.Button("Relatório", key="6")])
        self.__window = sg.Window("Agendamento").Layout(layout)

    def mostrar_menu(self, agendamentos):
        self.init_components(agendamentos)
        botao, valores = self.__window.Read()
        if botao is None:
            botao = 0
        agendamento = None
        for i in range(len(valores.values())):
            if valores[i]:
                agendamento = agendamentos[i][0]
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
        self.popup("Não há doses suficientes de vacina para o agendamento, o paciente foi movido para a lista de espera.")

    def mostra_agendamento(self, paciente_nome, enfermeiro_nome, ano, mes, dia, fabricante):
        self.popup("{}, você tem um agendamento para o dia {}/{}/{} com o enfermeiro {}, para ser vacinado com a vacina {}!".format(paciente_nome, dia, mes, ano, enfermeiro_nome, fabricante))

    def nao_ha_agendamento(self, cpf):
        self.popup("Não há nenhum agendamento com o cpf {}.".format(cpf))

    def removeu_agendamento(self, cpf):

        if cpf:
            self.popup(f"Não há nenhum agendamento com o cpf {cpf}")
        elif cpf is None:
            self.popup(msg)("Seu agendamento foi removido com sucesso!")

    def alterado(self):

        self.popup("Seu agendamento foi alterado com sucesso!")

    def vacina_primeira_dose(self, nome, vacina):

        if nome:
            self.popup(f"{nome} tomou a primeira dose da vacina {vacina}")
        else:
            self.popup("O paciente já tomou a primeira dose, agende a segunda dose!")
        
    def agendamento_segunda_dose(self, erro, nome=None, dia=None, mes=None, ano=None, hora=None):

        if erro == "nao_tomou_primeira_dose":
            self.popup("O paciente precisa tomar a primeira dose antes de agendar a segunda!")
        elif erro == "ja_tomou_segunda_dose":
            self.popup("O paciente já tomou a segunda dose!")
        elif erro == "ja_agendado":
            self.popup("O paciente já agendou a segunda!")
        else:
            self.popup(f"A segunda dose de {nome} está agendada para o dia {dia}/{mes}/{ano}, as {hora} horas!")

    def data_invalida_error(self, dia, mes, ano):

        self.popup(f"Data Inválida! Digite uma data a partir de {dia}/{mes}/{ano}!")

    def vacinado_completamente(self, erro, nome=None, vacina=None):

        if erro == "ja_vacinado":
            self.popup("O paciente já foi vacinado com a segunda dose.")
        else:
            self.popup(f"O paciente {nome} tomou a segunda dose da vacina {vacina}!")

    def relatorio(self, qtd_vacinas_aplicadas, vacinados_uma_dose, vacinados_duas_doses, pacientes_na_lista_de_espera, agendamento_prim, agendamento_seg):
        msg = ("")
        msg = msg + (f"Quantidade total de vacinas aplicadas: {qtd_vacinas_aplicadas} \n")
        msg = msg + (f"Quantidade de pessoas que tomaram apenas uma dose: {vacinados_uma_dose} \n")
        msg = msg + (f"Quantidade de pessoas que tomaram as duas doses: {vacinados_duas_doses} \n")
        msg = msg + (f"Quantidade de pessoas que esperam na fila de vacinação: {pacientes_na_lista_de_espera} \n")
        msg = msg + (f"Quantidade de pessoas com a primeira dose agendada: {agendamento_prim} \n")
        msg = msg + (f"Quantidade de pessoas com a segunda dose agendada: {agendamento_seg} \n")
        self.popup(msg)

    def popup(self, msg):
        sg.Popup("", "{}".format(msg))

    def close(self):
        self.__window.Close()
