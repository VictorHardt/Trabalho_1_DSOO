from model.vacina import Vacina
from view.telaVacina import TelaVacina

class ControladorVacina:
    def __init__(self):
        self.__vacinas = []
        self.__tela = TelaVacina()

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_vacina, 2: self.add_doses, 3: self.excluir, 4: self.alterar, 5: self.qtd_doses_cada_fabricante, 0: self.retorna}

        while True:
            opcao_escolhida = self.__tela.mostrar_menu()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def cadastra_vacina(self):
        dados_vacina = self.__tela.recebe_dados_vacina()

        vacina = Vacina(dados_vacina["fabricante"], dados_vacina["quantidade de doses"])

        for i in self.__vacinas:
            if "fabricante" == vacina.fabricante:
                self.__tela.vacina_repetida(vacina.fabricante)
            else:
                self.__vacinas.append(vacina)

    def add_doses(self, fabricante: str, quantidade: int):
        if isinstance(fabricante, str):
            self.__fabricante = fabricante
        if isinstance(quantidade, int):
            self.__quantidade = quantidade

        pass

    def excluir(self):
        pass

    def alterar(self):
        pass

    def qtd_doses_total(self):
        pass

    def qtd_doses_cada_fabricante(self):
        pass

    def tem_dose_disponivel(self):
        pass

    def retorna_vacina_para_agendamento(self):

        vacina = None
        i = 0
        while vacina is None and i < len(self.__vacinas):
            if self.__vacinas[i].qtd_doses >= 2:
                vacina = self.__vacinas[i]
                vacina.qtd_doses(vacina.qtd_doses - 2)
        return vacina

    def retorna(self):
        pass