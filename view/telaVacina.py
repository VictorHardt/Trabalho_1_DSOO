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
        qtd_doses = int(input("Quantidade de doses: "))

        return {"fabricante": fabricante, "qtd_doses": qtd_doses}

    def vacina_repetida(self, fabricante):
        print("")
        print("A vacina com fabricante {} já está na lista de vacinas! ".format(fabricante))

    def vacina_nao_existe(self, fabricante):
        print("")
        print("A vacina com fabricante {} ainda não existe! Por favor faça o cadastro! ".format(fabricante))

    def mostrar_vacinas(self, dados_vacina):
        print("Fabricante: ", dados_vacina["fabricante"])
        print("Quantidade de doses: ", dados_vacina["quantidade de doses"])
        print()

    def adiconar_doses(self):
        fabricante = self.ler_string("As doses adicionadas são de qual fabricante?: ")
        qtd_doses = int(input("Quantidade de doses adicionadas: "))

        return {"fabricante": fabricante, "qtd_doses": qtd_doses}

    def excluir_doses(self):
        fabricante = self.ler_string("As doses excluídas são de qual fabricante?: ")
        qtd_doses = int(input("Quantidade de doses excluídas: "))

        return {"fabricante": fabricante, "qtd_doses": qtd_doses}

    def alterar_doses(self):
        fabricante = self.ler_string("As doses que serão alteradas são de qual fabricante?: ")
        qtd_doses = int(input("Nova quantidade de doses: "))

        return {"fabricante": fabricante, "qtd_doses": qtd_doses}
