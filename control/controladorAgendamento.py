from model.agendamento import Agendamento
from view.telaAgendamento import TelaAgendamento
from control.controladorVacina import ControladorVacina
from control.controladorEnfermeiro import ControladorEnfermeiro
from control.controladorPaciente import ControladorPaciente
from datetime import datetime
from datetime import timedelta

class ControladorAgendamento:
    def __init__(self, controlador_vacina, controlador_paciente, controlador_enfermeiro):
        self.__tela = TelaAgendamento()
        self.__continuar = True
        self.__agendamentos = []
        self.__controlador_vacina = controlador_vacina
        self.__controlador_paciente = controlador_paciente
        self.__controlador_enfermeiro = controlador_enfermeiro
        self.__pacientes_que_tomaram_uma_dose = []
        self.__pacientes_completamente_vacinados = []
        self.__qtd_vacinas_aplicadas = 0
        self.__pacientes_na_lista_de_espera = []
        self.__pacientes_com_agendamento = []

    def abre_tela(self):

        self.__continuar = True
        lista_opcoes = {
            1: self.novo_agendamento, 
            2: self.checa_agendamento, 
            3: self.remove_agendamento, 
            4: self.altera_agendamento,
            5: self.vacina_primeira_dose,
            6: self.agenda_segunda_dose,
            7: self.vacina_segunda_dose,
            8: self.lista_pacientes_uma_dose,
            9: self.lista_pacientes_duas_doses,
            10: self.lista_pacientes_na_lista_de_espera,
            11: self.relatorio,
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
            self.__tela.enfermeiro_nao_existe_error(dados_agendamento["nome_enfermeiro"])
        elif vacina is None:
            self.__tela.sem_estoque_de_vacina_error()
            if paciente:
                self.__pacientes_na_lista_de_espera.append(paciente)
        else:
            agendamento = Agendamento(data, hora, enfermeiro, paciente, vacina)
            self.__agendamentos.append(agendamento)
            if paciente in self.__pacientes_na_lista_de_espera:
                self.__pacientes_na_lista_de_espera.remove(paciente)
            self.__pacientes_com_agendamento.append(paciente)
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
            self.__pacientes_com_agendamento.remove(agendamento.paciente)
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
                agendamento.data = nova_data
                self.__tela.alterado()
            elif opcao_escolhida == 2: #muda a hora
                nova_hora = self.__tela.escolher_hora()
                agendamento.hora = nova_hora
                self.__tela.alterado()
            elif opcao_escolhida == 3: #muda o enfermeiro
                nome_enfermeiro = self.__tela.escolher_enfermeiro()
                enfermeiro = self.__controlador_enfermeiro.retorna_enfermeiro(nome_enfermeiro)
                if enfermeiro:
                    agendamento.enfermeiro = enfermeiro
                    self.__tela.alterado()
                else:
                    self.__tela.enfermeiro_nao_existe_error(nome_enfermeiro)
            else: #muda o paciente
                cpf_paciente = self.__tela.escolher_paciente()
                paciente = self.__controlador_paciente.retorna_paciente(cpf_paciente)
                if paciente:
                    self.__pacientes_com_agendamento.remove(agendamento.paciente)
                    agendamento.paciente = paciente
                    self.__pacientes_com_agendamento.append(paciente)
                    self.__tela.alterado()
                else:
                    self.__tela.paciente_nao_existe_error(cpf_paciente)
        else:
            self.__tela.nao_ha_agendamento(cpf)

    def lista_agendamentos(self):

        agendamentos = []
        for agendamento in self.__agendamentos:
            string = f"Paciente: {agendamento.paciente.nome}, Enfermeiro: {agendamento.enfermeiro.nome}, Data: {agendamento.data.day}/{agendamento.data.month}/{agendamento.data.year}, Vacina: {agendamento.vacina.fabricante}."
            agendamentos.append(string)
        self.__tela.mostrar_agendamentos(agendamentos)

    def retorna_agendamento(self, cpf):

        agendamento = None
        i = 0
        while agendamento == None and i<len(self.__agendamentos):
            if cpf == self.__agendamentos[i].paciente.cpf:
                agendamento = self.__agendamentos[i]
            i += 1   
        return agendamento

    def vacina_primeira_dose(self):

        cpf = self.__tela.recebe_cpf()
        agendamento = self.retorna_agendamento(cpf)

        if agendamento and not agendamento.vacinado_primeira_dose:
            agendamento.vacinado_primeira_dose = True
            self.__pacientes_que_tomaram_uma_dose.append(agendamento.paciente)
            self.__pacientes_com_agendamento.remove(agendamento.paciente)
            self.__tela.vacina_primeira_dose(agendamento.paciente.nome, agendamento.vacina.fabricante)
            self.__qtd_vacinas_aplicadas =+ 1
        elif agendamento and agendamento.vacinado_primeira_dose:
            self.__tela.vacina_primeira_dose(None, None)
        else:
            self.__tela.nao_ha_agendamento(cpf)

    def agenda_segunda_dose(self):

        cpf = self.__tela.recebe_cpf()
        agendamento = self.retorna_agendamento(cpf)

        if agendamento and agendamento.vacinado_primeira_dose and not agendamento.vacinado_completamente and agendamento.data_segunda_dose is None:
            data_valida = False
            while not data_valida:
                data = self.__tela.escolher_data()
                if data >= agendamento.data + timedelta(20):
                    agendamento.data_segunda_dose = data
                    data_valida = True
                    hora = self.__tela.escolher_hora()
                    agendamento.hora_segunda_dose = hora
                    self.__tela.agendamento_segunda_dose(None, agendamento.paciente.nome, data.day, data.month, data.year, hora)
                else:
                    data_val = agendamento.data + timedelta(20)
                    self.__tela.data_invalida_error(data_val.day, data_val.month, data_val.year)
        elif agendamento and not agendamento.vacinado_primeira_dose:
            self.__tela.agendamento_segunda_dose("nao_tomou_primeira_dose")
        elif agendamento and agendamento.vacinado_completamente:
            self.__tela.agendamento_segunda_dose("ja_tomou_segunda_dose")
        elif agendamento and agendamento.data_segunda_dose is not None:
            self.__tela.agendamento_segunda_dose("ja_agendado")
        else:
            self.__tela.nao_ha_agendamento(cpf)

    def vacina_segunda_dose(self):
        cpf = self.__tela.recebe_cpf()
        agendamento = self.retorna_agendamento(cpf)

        if agendamento:
            if agendamento.data_segunda_dose and not agendamento.vacinado_completamente:
                agendamento.vacinado_completamente = True
                self.__pacientes_que_tomaram_uma_dose.remove(agendamento.paciente)
                self.__pacientes_completamente_vacinados.append(agendamento.paciente)
                self.__tela.vacinado_completamente(None, agendamento.paciente.nome, agendamento.vacina.fabricante)
                self.__qtd_vacinas_aplicadas =+ 1
            elif agendamento.vacinado_completamente:
                self.__tela.vacinado_completamente("ja_vacinado")
            elif agendamento.data_segunda_dose is None:
                self.__tela.vacinado_completamente("sem_agendamento")
        else:
            self.__tela.nao_ha_agendamento(cpf)

    def lista_pacientes_uma_dose(self):

        pacientes = []
        for paciente in self.__pacientes_que_tomaram_uma_dose:
            string = (f"Paciente: {paciente.nome} / CPF: {paciente.cpf}")
            pacientes.append(string)
        self.__tela.lista_pacientes(pacientes)

    def lista_pacientes_duas_doses(self):

        pacientes = []
        for paciente in self.__pacientes_completamente_vacinados:
            string = (f"Paciente: {paciente.nome} / CPF: {paciente.cpf}")
            pacientes.append(string)
        self.__tela.lista_pacientes(pacientes)

    def lista_pacientes_na_lista_de_espera(self):

        pacientes = []
        for paciente in self.__pacientes_na_lista_de_espera:
            string = (f"Paciente: {paciente.nome} / CPF: {paciente.cpf}")
            pacientes.append(string)
        self.__tela.lista_pacientes(pacientes)

    def relatorio(self):
        qtd_vacinas_aplicadas = self.__qtd_vacinas_aplicadas
        vacinados_uma_dose = len(self.__pacientes_que_tomaram_uma_dose)
        vacinados_duas_doses = len(self.__pacientes_completamente_vacinados)
        pacientes_na_lista_de_espera = len(self.__pacientes_na_lista_de_espera)
        pacientes_com_agendamento = len(self.__pacientes_com_agendamento)
        self.__tela.relatorio(qtd_vacinas_aplicadas, vacinados_uma_dose, vacinados_duas_doses, pacientes_na_lista_de_espera, pacientes_com_agendamento)

    def retorna(self):
        self.__continuar = False