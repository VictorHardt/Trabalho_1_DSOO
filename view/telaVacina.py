from view.abstractTela import AbstractTela

class TelaVacina(AbstractTela):
    def __init__(self):
        pass

    def mostrar_menu(self):
        print("")
        print("-------- Vacina ----------")
        print("")
        print("1 - Cadastrar vacina")
        print("2 - Adicionar doses de vacina")
        print("3 - Excluir doses de vacina")
        print("4 - Alterar doses de vacina")
        print("5 - Exibir quantidade total de doses de vacina disponíveis por fabricante")
        print("6 - Cadastrar local de armazenamento")
        print("0 - Retornar")

        return self.ler_numero([1,2,3,4,5,6,0])

    def recebe_dados_vacina(self):
        fabricante = self.ler_string("Fabricante: ")
        qtd_doses = self.ler_numero(None, "Quantidade de doses: ")
        local_armazenamento = self.ler_string("Digite o local de armazenamento da vacina: ")

        return {"fabricante": fabricante, "qtd_doses": qtd_doses,"local_armazenamento": local_armazenamento}

    def recebe_dados_amazenamento(self):
        local_armazenamento = self.ler_string("Qual é o local de armazenamento: ")
        temperatura = self.ler_numero(None, ("Qual a temperatura de armazento deste local: "))

        return {"local_armazenamento": local_armazenamento, "temperatura": temperatura}

    def local_armazenamento_ja_cadastrado(self, local):
        print("")
        print(f"O local de armazenamento {local} já foi cadastrado anteriormente!")
        input("")

    def local_armazenamento_nao_cadastrado(self, local):
        print("")
        print(f"Não foi possível realizar o cadastro pois o local de armazenamento {local} ainda não foi cadastrado")
        input("")

    def vacina_repetida(self, fabricante):
        print("")
        print("A vacina com fabricante {} já está na lista de vacinas! ".format(fabricante))
        input("")

    def vacina_nao_existe(self, fabricante):
        print("")
        print("A vacina com fabricante {} ainda não existe! Por favor faça o cadastro! ".format(fabricante))
        input("")

    def mostrar_vacinas(self, dados_vacina):
        print("")
        print("Fabricante: ", dados_vacina["fabricante"])
        print("Quantidade de doses: ", dados_vacina["quantidade de doses"])
        input("")

    def adiconar_doses(self):
        fabricante = self.ler_string("As doses adicionadas são de qual fabricante?: ")
        qtd_doses = self.ler_numero(None, "Quantidade de doses adicionadas: ")

        return {"fabricante": fabricante, "qtd_doses": qtd_doses}

    def excluir_doses(self):
        fabricante = self.ler_string("As doses excluídas são de qual fabricante?: ")
        qtd_doses = self.ler_numero(None, "Quantidade de doses excluídas: ")

        return {"fabricante": fabricante, "qtd_doses": qtd_doses}

    def alterar_doses(self):
        fabricante = self.ler_string("As doses que serão alteradas são de qual fabricante?: ")
        qtd_doses = self.ler_numero(None, "Nova quantidade de doses: ")

        return {"fabricante": fabricante, "qtd_doses": qtd_doses}

    