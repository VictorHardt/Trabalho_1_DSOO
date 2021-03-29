class TelaPaciente:
    def __init__(self, controlador_paciente: ControladorPaciente):
        self.__controlador_paciente = controlador_paciente

    def mostrar_menu(self):
        print("-------- Paciente ----------")
        print("Escolha a opcao")
        print("1 - Cadastrar paciente")
        print("2 - Alterar dados do paciente")
        print("3 - Verificar se paciente possui agendamento")
        print("4 - Verificar fila de pacientes")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def recebe_idade(self): #int
        pass

    def recebe_dados_paciente(self):
        pass