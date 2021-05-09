from model.agendamento import Agendamento
from view.telaAgendamento import TelaAgendamento
from control.controladorVacina import ControladorVacina
from control.controladorEnfermeiro import ControladorEnfermeiro
from control.controladorPaciente import ControladorPaciente
from datetime import datetime
from datetime import timedelta
from persistence.agendamentoDAO import AgendamentoDAO
from persistence.listaDeEsperaDAO import ListaDeEsperaDAO
from exception.agendamentoNaoSelecionadoException import AgendamentoNaoSelecionadoException

class ControladorAgendamento:
    def __init__(self, controlador_vacina, controlador_paciente, controlador_enfermeiro):
        self.__tela = TelaAgendamento()
        self.__continuar = True
        self.__dao = AgendamentoDAO()
        self.__lista_de_espera_dao  = ListaDeEsperaDAO()
        self.__agendamento = None
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
            2: self.altera_agendamento, 
            3: self.remove_agendamento,
            4: self.vacina,
            5: self.vacinados,
            6: self.lista_pacientes_na_lista_de_espera,
            7: self.relatorio,
            0: self.retorna}

        while self.__continuar:            
            enfermeiros = self.__dao.get_all()
            agdms = []
            for enfermeiro in enfermeiros:
                agdms.append([agendamento.paciente.nome, agendamento.paciente.cpf, agendamento.data])
            opcao_escolhida = self.__tela.mostrar_menu(agdms)
            agendamento = opcao_escolhida[1]
            if agendamento:
                self.__agendamento = self.__dao.get(agendamento)
            funcao_escolhida = lista_opcoes[opcao_escolhida[0]]
            funcao_escolhida()

    def novo_agendamento(self):

        dados_agendamento = self.__tela.recebe_dados_agendamento()
        if dados_agendamento[1] != 0:
            if dados_agendamento[0] == 1:
                paciente = self.__controlador_paciente.retorna_paciente(dados_agendamento[1]["cpf"])
                enfermeiro = self.__controlador_enfermeiro.retorna_enfermeiro(dados_agendamento[1]["cpf_enfermeiro"])
                data = dados_agendamento[1]["data"]
                hora = dados_agendamento[1]["hora"]
                vacina = self.__controlador_vacina.retorna_vacina_para_agendamento()
                if paciente is None:
                    self.__tela.paciente_nao_existe_error(dados_agendamento[1]["cpf"]) 
                elif enfermeiro is None:
                    self.__tela.enfermeiro_nao_existe_error(dados_agendamento[1]["cpf_enfermeiro"])
                elif vacina is None:
                    self.__tela.sem_estoque_de_vacina_error()
                    if paciente:
                        self.__lista_de_espera_dao.add(paciente)
                else:
                    agendamento = Agendamento(data, hora, enfermeiro, paciente, vacina)
                    self.__dao.append(agendamento)
                    if self.__lista_de_espera_dao.get(paciente.cpf):
                        self.__lista_de_espera_dao.remove(paciente.cpf)
                    self.__tela.mostra_agendamento(agendamento.paciente.nome, agendamento.enfermeiro.nome, agendamento.data.year, agendamento.data.month, agendamento.data.day, agendamento.vacina.fabricante)

            elif dados_agendamento[0] == 2:
                agendamento = self.__dao.get(dados_agendamento['cpf'])
                if agendamento and agendamento.vacinado_primeira_dose and not agendamento.vacinado_completamente and agendamento.data_segunda_dose is None:
                    data = self.__dados_agendamento['data']
                    if data >= agendamento.data + timedelta(20):
                        agendamento.data_segunda_dose = data
                        hora = self.__dados_agendamento['hora']
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

    def remove_agendamento(self):
        try:
            if self.__agendamento:
                self.__dao.remove(self.__agendamento.paciente.cpf)
            else:
                raise AgendamentoNaoSelecionadoException
        except AgendamentoNaoSelecionadoException:
            pass

    def altera_agendamento(self):
        
        try:
            if self.__agendamento:
                dados_agendamento = self.__tela.recebe_dados_agendamento()
                if dados_agendamento[1] != 0:
                    if dados_agendamento[0] == 1:
                        pass
                    elif dados_agendamento[0] == 2:
                        pass
            else:
                raise AgendamentoNaoSelecionadoException
        except AgendamentoNaoSelecionadoException:
            pass

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
        for paciente in self.__dao.get_all():
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

    def vacina(self):
        pass

    def vacinados(self):
        pass

    def retorna(self):
        self.__continuar = False