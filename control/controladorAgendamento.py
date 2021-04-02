from model.agendamento import Agendamento
from view.telaAgendamento import TelaAgendamento
from control.controladorVacina import ControladorVacina
from control.controladorEnfermeiro import ControladorEnfermeiro
from control.controladorPaciente import ControladorPaciente

class ControladorAgendamento:
    def __init__(self, controlador_vacina, controlador_paciente, controlador_enfermeiro):
        self.__tela = TelaAgendamento()
        self.__continuar = True
        self.__agendamentos = []
        self.__controlador_vacina = controlador_vacina
        self.__controlador_paciente = controlador_paciente
        self.__controlador_enfermeiro = controlador_enfermeiro

    def abre_tela(self):

        self.__continuar = True
        lista_opcoes = {
            1: self.novo_agendamento, 
            2: self.checa_agendamento, 
            3: self.remove_agendamento, 
            4: self.altera_agendamento, 
            0: self.retorna
        }
        while self.__continuar:            
            opcao_escolhida = self.__tela.mostrar_menu()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def novo_agendamento(self):
        
        dados_agendamento = self.__tela.recebe_dados_agendamento()
        paciente = self.__controlador_paciente.retorna_paciente(dados_agendamento["cpf"])
        enfermeiro = self.__controlador_enfermeiro.retorna_enfermeiro(dados_agendamento["nome_enfermeiro"])
        data = dados_agendamento["data"]
        hora = dados_agendamento["hora"]
        vacina = self.__controlador_vacina.retorna_vacina_para_agendamento()
        if paciente is None:
            self.__tela.paciente_nao_existe_error(dados_agendamento["cpf"])
        elif enfermeiro is None:
            self.__tela.enfermeiro_nao_existe_error(dados_agendamento["nome"])
        elif vacina is None:
            self.__tela.sem_estoque_de_vacina_error()
        else:
            agendamento = Agendamento(data, hora, enfermeiro, paciente, vacina)
            self.__agendamentos.append(agendamento)
        

    def checa_agendamento(self):
        pass

    def remove_agendamento(self):
        pass

    def altera_agendamento(self):
        pass

    def retorna(self):
        self.__continuar = False