from view.abstractTela import AbstractTela

class TelaPaciente(AbstractTela):
    def __init__(self):
        pass

    def mostrar_menu(self):
        print("-------- Paciente ----------")
        print("Escolha a opcao")
        print("1 - Cadastrar paciente")
        print("2 - Alterar dados do paciente")
        print("3 - Excluir paciente")
        print("0 - Retornar")

        return self.ler_numero([1,2,3,0])

    def recebe_dados_paciente(self):
        nome = self.ler_string("Nome: ")
        idade = 160
        while idade > 150:
            idade = self.ler_numero(None, "Idade: ")
            if idade > 150:
                print("Digite uma idade válida entre 0 e 150")
        cpf = self.ler_string("CPF: ")

        return {"nome": nome, "idade": idade, "CPF": cpf}

    def cpf_duplicado_error(self, cpf):
        print("")
        print("O enfermeiro com cpf {} já está na lista de enfermeiros! ".format(cpf))