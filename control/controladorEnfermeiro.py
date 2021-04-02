from model.enfermeiro import Enfermeiro
from view.telaEnfermeiro import TelaEnfermeiro

class ControladorEnfermeiro:
    def __init__(self):
        self.__tela = TelaEnfermeiro()
        self.__enfermeiros = []
        self.__continuar = True
        
    def abre_tela(self):

        self.__continuar = True
        lista_opcoes = {
            1: self.cadastra_enfermeiro,
            2: self.altera_dados_enfermeiro,
            3: self.exlui_enfermeiro, 
            4: self.lista_agendamentos, 5: self.lista_pacientes, 0: self.retorna
        }
        while True:            
            opcao_escolhida = self.__tela.mostrar_menu()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def cadastra_enfermeiro(self):

        cadastrou = False
        while not cadastrou:
            dados_paciente = self.__tela.recebe_dados_enfermeiro()
            nome = dados_paciente["nome"]
            cpf = dados_paciente["cpf"]
            duplicado = False
            i = 0
            while duplicado is not True and i < len(self.__enfermeiros):
                if self.__enfermeiros[i].cpf == cpf:
                    duplicado = True
            if duplicado is not True:
                self.__enfermeiros.append(Enfermeiro(nome, cpf))
                cadastrou = True
            else:
                self.__tela.cpf_duplicado_error(cpf)

    def altera_dados_enfermeiro(self):
        pass

    def exlui_enfermeiro(self):
        pass

    def lista_agendamentos(self):
        pass

    def lista_pacientes(self):
        pass

    def retorna(self):
        self.__continuar = False