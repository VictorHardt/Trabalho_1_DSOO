from model.enfermeiro import Enfermeiro
from view.telaEnfermeiro import TelaEnfermeiro
from model.paciente import Paciente

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
            4: self.lista_enfermeiros,
            5: self.lista_pacientes,
            0: self.retorna
        }
        while self.__continuar:            
            opcao_escolhida = self.__tela.mostrar_menu()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def cadastra_enfermeiro(self):

        cadastrou = False
        while not cadastrou:
            dados_enfermeiro = self.__tela.recebe_dados_enfermeiro()
            nome = dados_enfermeiro["nome"]
            cpf = dados_enfermeiro["cpf"]
            duplicado = False
            i = 0
            while duplicado is not True and i < len(self.__enfermeiros):
                if self.__enfermeiros[i].cpf == cpf:
                    duplicado = True
                i += 1
            if duplicado is not True:
                self.__enfermeiros.append(Enfermeiro(nome, cpf))
                cadastrou = True
            else:
                self.__tela.cpf_duplicado_error(cpf)

    def altera_dados_enfermeiro(self):
        
        dados_alteracao = self.__tela.altera_dados_enfermeiro()
        enfermeiro = self.retorna_enfermeiro(dados_alteracao["nome"])

        if enfermeiro:
            if dados_alteracao["opcao_escolhida"] == 1:
                enfermeiro.nome = self.__tela.recebe_nome()
                self.__tela.alterado()
            else:
                cpf = self.__tela.recebe_cpf()
                duplicado = False
                i = 0
                while duplicado is not True and i < len(self.__enfermeiros):
                    if self.__enfermeiros[i].cpf == cpf:
                        duplicado = True
                if not duplicado:
                    enfermeiro.cpf = cpf
                    self.__tela.alterado()
                else:
                    self.__tela.cpf_duplicado_error(cpf)


    def exlui_enfermeiro(self):
        
        dados_enfermeiro = self.__tela.recebe_dados_enfermeiro()
        enfermeiro = self.retorna_enfermeiro(dados_enfermeiro["nome"])

        if enfermeiro:
            self.__enfermeiros.remove(enfermeiro)
            self.__tela.removido(enfermeiro.nome)
        else:
            self.__tela.removido(None)

    def lista_enfermeiros(self):

        enfermeiros = []
        for enfermeiro in self.__enfermeiros:
            string = f"{enfermeiro.nome} - {enfermeiro.cpf}"
            enfermeiros.append(string)
        self.__tela.mostrar_enfermeiros(enfermeiros)

    def retorna_enfermeiro(self, nome_enfermeiro:str) -> Enfermeiro:
        enf = None
        for enfermeiro in self.__enfermeiros:
            if enfermeiro.nome == nome_enfermeiro:
                enf = enfermeiro
        return enf

    def add_paciente(self, paciente: Paciente, enfermeiro: Enfermeiro):

        i = 0
        duplicado = False
        pacientes = enfermeiro.pacientes
        while i < len(pacientes) and duplicado is False:
            if pacientes[i].nome == paciente.nome:
                duplicado == True
            i += 1
        if duplicado is not True:
            enfermeiro.pacientes.append(paciente)

    def lista_pacientes(self):
        enfermeiro = self.retorna_enfermeiro(self.__tela.recebe_nome())
        for paciente in enfermeiro.pacientes:
            self.__tela.mostra_paciente(f"Paciente {paciente.nome} - Cpf {paciente.cpf}")

    def retorna(self):
        self.__continuar = False