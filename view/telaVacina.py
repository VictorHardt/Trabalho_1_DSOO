from view.abstractTela import AbstractTela

class TelaVacina(AbstractTela):
    def __init__(self):
        pass

    def mostrar_menu(self):
        print("-------- Vacina ----------")
        print("Escolha a opcao")
        print("1 - Cadastrar vacina")
        print("2 - Adicionar doses de vacina")
        print("3 - Excluir doses de vacina")
        print("4 - Alterar doses de vacina")
        print("5 - Exibir quantidade total de doses de vacina disponíveis por fabricante")
        print("0 - Retornar")

        return self.ler_numero([1,2,3,4,5,0])

    def recebe_dados_vacina(self):
        fabricante = self.ler_string("Fabricante: ")
        quantidade_doses = self.ler_string("Quantidade de doses: ")

        return {"fabricante": fabricante, "quantidade de doses": quantidade_doses}

    def vacina_repetida(self, fabricante):
        print("")
        print("A vacina com fabricante {} já está na lista de vacinas! ".format(fabricante))

    def mostrar_vacinas(self):
        pass