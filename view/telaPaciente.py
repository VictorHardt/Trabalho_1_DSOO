from view.abstractTela import AbstractTela
from control.controladorPaciente import ControladorPaciente

class TelaPaciente(AbstractTela):
    def __init__(self, controlador_paciente: ControladorPaciente):
        self.__controlador_paciente = controlador_paciente

    def mostrar_menu(self):
        print("-------- Paciente ----------")
        print("Escolha a opcao")
        print("1 - Cadastrar paciente")
        print("2 - Alterar dados do paciente")
        print("3 - Excluir paciente")
        print("4 - Verificar se paciente possui agendamento")
        print("5 - Verificar fila de pacientes")
        print("0 - Retornar")

        return self.ler_numero([1,2,3,4,0])

    def recebe_dados_paciente(self):
        nome = self.ler_string("Nome: ")
        idade = self.ler_string("Idade: ")
        cpf = self.ler_string("CPF: ")

        return {"nome": nome, "idade": idade, "CPF": cpf}

    def cpf_duplicado_error(self, cpf):
        print("")
        print("O enfermeiro com cpf {} já está na lista de enfermeiros! ".format(cpf))