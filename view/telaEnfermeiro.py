from view.abstractTela import AbstractTela
from control.controladorEnfermeiro import ControladorEnfermeiro

class TelaEnfermeiro(AbstractTela):
    def __init__(self, controlador_enfermeiro : ControladorEnfermeiro):
        self.__controlador_enfermeiro = controlador_enfermeiro

    def mostrar_menu(self):
        
        print("")
        print("------------Menu de Agendamentos------------")
        print("")
        print("1 : Cadastra Enfermeiro")
        print("2 : Altera Dados do Enfermeiro")
        print("3 : Exclui Enfermeiro")
        print("4 : Lista Agendamentos")
        print("5 : Lista Pacientes")
        print("0 : Retornar")
        print("")

        return self.ler_numero([1,2,3,4,5,0])
    
    def recebe_dados_enfermeiro(self):

        dados_enfermeiro = {}
        dados_enfermeiro["nome"] = self.ler_string("Digite o nome do enfermeiro: ")
        dados_enfermeiro["cpf"] = self.ler_string("Digite o cpf do enfermeiro: ")
        return dados_enfermeiro

    def cpf_duplicado_error(self, cpf):
        
        print("")
        print("O enfermeiro com cpf {} já está na lista de enfermeiros! ".format(cpf))


