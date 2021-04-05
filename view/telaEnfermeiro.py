from view.abstractTela import AbstractTela

class TelaEnfermeiro(AbstractTela):
    def __init__(self):
        pass

    def mostrar_menu(self):
        
        print("")
        print("------------ Enfermeiro ------------")
        print("")
        print("1 : Cadastra Enfermeiro")
        print("2 : Altera Dados do Enfermeiro")
        print("3 : Exclui Enfermeiro")
        print("4 : Lista Enfermeiros")
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
        input("")

    def altera_dados_enfermeiro(self):
        print("")

        dados_alteracao = {}
        dados_alteracao["nome"] = self.ler_string("Digite o nome do enfermeiro: ")
        print("")
        dados_alteracao["opcao_escolhida"] = self.ler_numero([1,2], "Digite 1 para alterar o nome, digite 2 para alterar o cpf")
        return dados_alteracao

    def recebe_nome(self):
        return self.ler_string("Digite o novo nome: ")

    def recebe_cpf(self):
        return self.ler_string("Digite o novo cpf: ")

    def alterado(self):
        print("")
        print("Os dados do enfermeiro foram atualizados com sucesso!")
        input("")

    def mostra_paciente(self, msg):
        print("")
        print(msg)
        input("")

    def removido(self, nome):
        print("")
        if nome:
            print(f"O enfermeiro {nome} foi removido com sucesso!")
        else:
            print("Não foi possível remover o cadastro do enfermeiro.")
        input("")

    def mostrar_enfermeiros(self, enfermeiros):
        print("")
        if len(enfermeiros) > 0:
            print("----- Lista de Enfermeiros -----")
            print("")
            print("NOME      CPF")
            for enfermeiro in enfermeiros:
                print(enfermeiro)
        else:
            print("Ainda não há enfermeiros cadastrados.")
        input("")
        