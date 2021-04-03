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
            self.__tela.mostra_agendamento(agendamento.paciente.nome, agendamento.enfermeiro.nome, agendamento.data.year, agendamento.data.month, agendamento.data.day, agendamento.vacina.fabricante)
        

    def checa_agendamento(self):

        cpf = self.__tela.recebe_cpf()
        agendamento = self.retorna_agendamento(cpf)
        if agendamento:
            self.__tela.mostra_agendamento(agendamento.paciente.nome, agendamento.enfermeiro.nome, agendamento.data.year, agendamento.data.month, agendamento.data.day, agendamento.vacina.fabricante)
        else:
            self.__tela.nao_ha_agendamento(cpf)


    def remove_agendamento(self):
        
        cpf = self.__tela.recebe_cpf()
        agendamento = self.retorna_agendamento(cpf)
        if agendamento:
            self.__agendamentos.remove(agendamento)
            self.__tela.removeu_agendamento(None)
        else:
            self.__tela.removeu_agendamento(cpf)

    def altera_agendamento(self):
        
        cpf = self.__tela.recebe_cpf()
        agendamento = self.retorna_agendamento(cpf)
        if agendamento:          
            opcao_escolhida = self.__tela.opcao_para_alteracao()
            if opcao_escolhida == 1: #muda a data
                nova_data = self.__tela.escolher_data()
                agendamento.data(nova_data)
                self.__tela.alterado()
            elif opcao_escolhida == 2: #muda a hora
                nova_hora = self.__tela.escolher_hora()
                agendamento.hora(nova_hora)
                self.__tela.alterado()
            elif opcao_escolhida == 3: #muda o enfermeiro
                nome_enfermeiro = self.__tela.escolher_enfermeiro()
                enfermeiro = self.__controlador_enfermeiro.retorna_enfermeiro(nome_enfermeiro)
                if enfermeiro:
                    agendamento.enfermeiro(enfermeiro)
                    self.__tela.alterado()
                else:
                    self.__tela.enfermeiro_nao_existe_error(nome_enfermeiro)
            else: #muda o paciente
                cpf_paciente = self.__tela.escolher_paciente()
                paciente = self.__controlador_paciente.retorna_paciente(cpf_paciente)
                if paciente:
                    agendamento.paciente(paciente)
                    self.__tela.alterado()
                else:
                    self.__tela.paciente_nao_existe_error(cpf_paciente)
        else:
            self.__tela.nao_ha_agendamento(cpf)

    def retorna_agendamento(self, cpf):

        agendamento = None
        i = 0
        while agendamento == None and i<len(self.__agendamentos):
            if cpf == self.__agendamentos[i].paciente.cpf:
                agendamento = self.__agendamentos[i]
            i += 1   
        return agendamento

    def retorna(self):
        self.__continuar = False