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

    def abre_tela(self):

        self.__continuar = True
        lista_opcoes = {
            1: self.novo_agendamento, 
            2: self.altera_agendamento, 
            3: self.remove_agendamento,
            4: self.vacina,
            5: self.lista_pacientes_na_lista_de_espera,
            6: self.relatorio,
            0: self.retorna}

        while self.__continuar:            
            agendamentos = list(self.__dao.get_all())
            agdms = []
            for agendamento in agendamentos:
                if agendamento.vacinado_primeira_dose and not agendamento.vacinado_completamente and agendamento.data_segunda_dose:
                    msg = ("Agendado p/ 2ª Dose")
                    agdms.append([agendamento.paciente.cpf, msg, agendamento.enfermeiro.nome, agendamento.data_segunda_dose, agendamento.hora_segunda_dose, agendamento.vacina.fabricante])
                elif agendamento.vacinado_completamente:
                    msg = ("Vacinado com 2 doses")
                    agdms.append([agendamento.paciente.cpf, msg, agendamento.enfermeiro.nome, agendamento.data_segunda_dose, agendamento.hora_segunda_dose, agendamento.vacina.fabricante])
                elif agendamento.vacinado_primeira_dose and agendamento.data_segunda_dose is None:
                    msg = ("Tomou uma dose")
                    agdms.append([agendamento.paciente.cpf, msg, agendamento.enfermeiro.nome, agendamento.data, agendamento.hora, agendamento.vacina.fabricante])
                else:
                    msg = ("Agendado p/ 1ª Dose")
                    agdms.append([agendamento.paciente.cpf, msg, agendamento.enfermeiro.nome, agendamento.data, agendamento.hora, agendamento.vacina.fabricante])
            opcao_escolhida = self.__tela.mostrar_menu(agdms)
            escolhido = opcao_escolhida[1]
            if escolhido:
                self.__agendamento = self.__dao.get(escolhido)
            funcao_escolhida = lista_opcoes[opcao_escolhida[0]]
            funcao_escolhida()

    def novo_agendamento(self):

        dados_agendamento = self.__tela.recebe_dados_agendamento()
        if dados_agendamento[1] != 0:
            if dados_agendamento[0] == 1:
                if self.__dao.get(dados_agendamento[1]["cpf"]) is None:
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
                        self.__dao.add(agendamento)
                        if self.__lista_de_espera_dao.get(paciente.cpf):
                            self.__lista_de_espera_dao.remove(paciente.cpf)
                        self.__tela.mostra_agendamento(agendamento.paciente.nome, agendamento.enfermeiro.nome, agendamento.data.year, agendamento.data.month, agendamento.data.day, agendamento.vacina.fabricante)
                else:
                    self.__tela.popup("Este cpf já possui um agendamento!")
            elif dados_agendamento[0] == 2:
                agendamento = self.__dao.get(dados_agendamento[1]['cpf'])
                if agendamento and agendamento.data_segunda_dose is None:
                    if agendamento.vacinado_primeira_dose and not agendamento.vacinado_completamente and agendamento.data_segunda_dose is None:
                        data = dados_agendamento[1]['data']
                        if data >= agendamento.data + timedelta(20):
                            agendamento.data_segunda_dose = data
                            hora = dados_agendamento[1]['hora']
                            agendamento.hora_segunda_dose = hora
                            self.__tela.agendamento_segunda_dose(None, agendamento.paciente.nome, data.day, data.month, data.year, hora)
                        else:
                            data_val = agendamento.data + timedelta(20)
                            self.__tela.data_invalida_error(data_val.day, data_val.month, data_val.year)
                    elif not agendamento.vacinado_primeira_dose:
                        self.__tela.agendamento_segunda_dose("nao_tomou_primeira_dose")
                    elif agendamento.vacinado_completamente:
                        self.__tela.agendamento_segunda_dose("ja_tomou_segunda_dose")
                    elif agendamento.data_segunda_dose is not None:
                        self.__tela.agendamento_segunda_dose("ja_agendado")
                elif agendamento and agendamento.data_segunda_dose:
                    self.__tela.popup("Este cpf já possui um agendamento!")              
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
                if not self.__agendamento.vacinado_completamente:
                    dados_agendamento = self.__tela.recebe_dados_agendamento()
                    if dados_agendamento[1] == 1:
                        self.__agendamento.enfermeiro = self.__controlador_enfermeiro.retorna_enfermeiro(dados_agendamento[1]["cpf_enfermeiro"])
                        self.__agendamento.data = dados_agendamento[1]["data"]
                        self.__agendamento.hora = dados_agendamento[1]["hora"]
                        if paciente is None:
                            self.__tela.paciente_nao_existe_error(dados_agendamento[1]["cpf"]) 
                        elif enfermeiro is None:
                            self.__tela.enfermeiro_nao_existe_error(dados_agendamento[1]["cpf_enfermeiro"])
                    elif dados_agendamento[0] == 2:
                        if dados_agendamento.paciente.cpf == dados_alteração[1]["cpf"]:
                            data = dados_agendamento[1]['data']
                            if data >= agendamento.data + timedelta(20):
                                agendamento.data_segunda_dose = data
                                hora = dados_agendamento[1]['hora']
                                agendamento.hora_segunda_dose = hora
                                self.__tela.agendamento_segunda_dose(None, agendamento.paciente.nome, data.day, data.month, data.year, hora)
                            else:
                                data_val = agendamento.data + timedelta(20)
                                self.__tela.data_invalida_error(data_val.day, data_val.month, data_val.year)
                            self.__dao.update()
                        else:
                            self.__tela.popup("O cpf inserido não é o mesmo do agendamento selecionado!")
                else:
                    self.__tela.popup("Não é possivel alterar um agendamento após a vacinação!")
            else:
                raise AgendamentoNaoSelecionadoException
        except AgendamentoNaoSelecionadoException:
            pass

    def lista_pacientes_na_lista_de_espera(self):

        pacientes = list(self.__lista_de_espera_dao.get_all())
        if len(pacientes) > 0:
            msg = ('')
            for paciente in pacientes:
                msg = msg + ("{} - {} \n".format(paciente.nome, paciente.cpf))
            self.__tela.popup(msg)
        else:
            self.__tela.popup("A lista de espera está vazia")

    def relatorio(self):
        agendamentos = list(self.__dao.get_all())
        qtd_vacinas_aplicadas = 0
        vacinados_uma_dose = 0
        vacinados_duas_doses = 0
        for agdm in agendamentos:
            if agdm.vacinado_primeira_dose and not agdm.vacinado_completamente:
                qtd_vacinas_aplicadas += 1
                vacinados_uma_dose += 1
            elif agdm.vacinado_completamente:
                qtd_vacinas_aplicadas += 2
                vacinados_duas_doses += 1
        pacientes_na_lista_de_espera = len(self.__lista_de_espera_dao.get_all())
        agendamento_prim = 0
        agendamento_seg = 0
        for agdm in agendamentos:
            if agdm.data_segunda_dose is None and not agdm.vacinado_completamente:
                agendamento_prim += 1
            elif agdm.data_segunda_dose is not None and not agdm.vacinado_completamente:
                agendamento_seg += 1
        self.__tela.relatorio(qtd_vacinas_aplicadas, vacinados_uma_dose, vacinados_duas_doses, pacientes_na_lista_de_espera, agendamento_prim, agendamento_seg)

    def vacina(self):
        agendamento = self.__agendamento
        try:    
            if agendamento:
                if not agendamento.vacinado_primeira_dose:
                    agendamento.vacinado_primeira_dose = True
                    self.__dao.update()
                    self.__tela.vacina_primeira_dose(agendamento.paciente.nome, agendamento.vacina.fabricante)
                elif agendamento.vacinado_primeira_dose and agendamento.data_segunda_dose is None:
                    self.__tela.vacina_primeira_dose(None, None)
                elif not agendamento.vacinado_completamente and agendamento.data_segunda_dose:
                    agendamento.vacinado_completamente = True
                    self.__dao.update()
                    self.__tela.vacinado_completamente(None, agendamento.paciente.nome, agendamento.vacina.fabricante)
                elif agendamento.vacinado_completamente:
                    self.__tela.vacinado_completamente("ja_vacinado")
            else:
                raise AgendamentoNaoSelecionadoException()
        except AgendamentoNaoSelecionadoException:
            pass

    def retorna(self):
        self.__continuar = False