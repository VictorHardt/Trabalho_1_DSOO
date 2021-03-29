class TelaVacina:
    def __init__(self, controlador_vacina: Cotrolador_vacina):
        self.__controlador_vacina = controlador_vacina

    def mostrar_menu(self):
        print("-------- Vacina ----------")
        print("Escolha a opcao")
        print("1 - Cadastrar vacina")
        print("2 - Adicionar doses de vacina")
        print("3 - Excluir doses de vacina")
        print("4 - Alterar doses de vacina")
        print("5 - Exibir quantidade total de doses de vacina disponíveis por fabricante")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def mostrar_vacinas(self):
        pass

    def recebe_dados_vacina(self):
        pass