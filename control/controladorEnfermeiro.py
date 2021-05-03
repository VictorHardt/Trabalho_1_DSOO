
from view.telaEnfermeiro import TelaEnfermeiro
from model.enfermeiro import Enfermeiro
from model.paciente import Paciente
from persistence.enfermeiroDAO import EnfermeiroDAO

class ControladorEnfermeiro:
    def __init__(self):
        self.__tela = TelaEnfermeiro()
        self.__dao = EnfermeiroDAO()
        self.__continuar = True
        
    def abre_tela(self):

        self.__continuar = True
        lista_opcoes = {
            1: self.cadastra_enfermeiro,
            2: self.altera_dados_enfermeiro,
            3: self.exlui_enfermeiro, 
            4: self.lista_enfermeiros,
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
            enfermeiro = self.__dao.get(cpf)
            if enfermeiro is None:
                self.__dao.add(Enfermeiro(nome, cpf))
                cadastrou = True
            else:
                self.__tela.cpf_duplicado_error(cpf)

    def altera_dados_enfermeiro(self):
        
        dados_alteracao = self.__tela.altera_dados_enfermeiro()
        enfermeiro = self.dao.get(dados_alteracao["cpf"])

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
        self.__dao.remove(dados_enfermeiro["cpf"])

    def lista_enfermeiros(self):

        enfermeiros = []
        lista_enfermeiros = self.__dao.get_all()
        for enfermeiro in lista_enfermeiros:
            string = f"{enfermeiro.nome} - {enfermeiro.cpf}"
            enfermeiros.append(string)
        self.__tela.mostrar_enfermeiros(enfermeiros)

    def retorna(self):
        self.__continuar = False
