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
        print("4 - Lista pacientes")
        print("0 - Retornar")

        return self.ler_numero([1,2,3,4,0])

    def recebe_dados_paciente(self):
        nome = self.ler_string("Nome: ")
        idade = 160
        while idade > 150:
            idade = self.ler_numero(None, "Idade: ")
            if idade > 150:
                print("Digite uma idade válida entre 0 e 150")
        cpf = self.ler_string("CPF: ")
        endereco = self.recebe_endereco()

        return {"nome": nome, "idade": idade, "CPF": cpf, "endereco": endereco}

    def cpf_duplicado_error(self, cpf):
        print("")
        print("O paciente com cpf {} já está na lista de pacientes! ".format(cpf))
        input("")

    def cpf_nao_existe(self, cpf):
        print("")
        print("O paciente com cpf {} não está na lista de pacientes! ".format(cpf))
        input("")

    def recebe_endereco(self):
        endereco = {}
        endereco["cidade"] = self.ler_string("Cidade: ")
        endereco["rua"] = self.ler_string("Rua: ")
        endereco["numero"] = self.ler_numero(None, "Numero: ")
        return endereco

    def alterar(self):
        cpf = self.ler_string("Digite o CPF do paciente a ser alterado: ")
        nome = self.ler_string("Novo nome: ")
        idade = 160
        while idade > 150:
            idade = self.ler_numero(None, "Idade: ")
            if idade > 150:
                print("Digite uma idade válida entre 0 e 150")
        endereco = self.recebe_endereco()

        return {"nome": nome, "idade": idade, "CPF": cpf, "endereco": endereco}

    def excluir_paciente(self):
        cpf = self.ler_string("Digite o CPF do paciente a ser excluído: ")

        return {"CPF": cpf}

    def listar_pacientes(self, dados_paciente):
        print("")
        print("Nome: ", dados_paciente["nome"])
        print("CPF: ", dados_paciente["CPF"])
        print("Idade: ", dados_paciente["idade"])
        print("Cidade: ", dados_paciente["cidade"])
        print("Rua: ", dados_paciente["rua"])
        print("Número: ", dados_paciente["numero"])

        input("")


        #print("Cidade: ", dados_paciente["cidade"])
        #print("Rua: ", dados_paciente["rua"])
        #print("Número: ", dados_paciente["numero"])
