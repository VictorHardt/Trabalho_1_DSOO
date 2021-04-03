from model.vacina import Vacina
from view.telaVacina import TelaVacina

class ControladorVacina:
    def __init__(self):
        self.__vacinas = []
        self.__tela = TelaVacina()
        self.__continuar = True

    def abre_tela(self):
        self.__continuar = True
        lista_opcoes = {
            1: self.cadastra_vacina,
            2: self.add_doses,
            3: self.excluir,
            4: self.alterar,
            5: self.qtd_doses_cada_fabricante,
            0: self.retorna}

        while self.__continuar:
            opcao_escolhida = self.__tela.mostrar_menu()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def cadastra_vacina(self):

        dados_vacina = self.__tela.recebe_dados_vacina()

        fabricante = dados_vacina["fabricante"]
        qtd_doses = dados_vacina["qtd_doses"]

        vacina_atual = Vacina(fabricante, qtd_doses)
        repeticao = 0
        for vacina in self.__vacinas:
            if vacina.fabricante == vacina_atual.fabricante:
                repeticao += 1
                return self.__tela.vacina_repetida(fabricante)
        if repeticao == 0:
            self.__vacinas.append(vacina_atual)

    def add_doses(self):
        dados_vacina = self.__tela.adiconar_doses()

        fabricante = dados_vacina["fabricante"]
        qtd_doses = dados_vacina["qtd_doses"]
        vacina_atual = Vacina(fabricante, qtd_doses)
        adicionou = False

        for vacina in self.__vacinas:
            if vacina.fabricante == vacina_atual.fabricante:
                vacina.qtd_doses += vacina_atual.qtd_doses
                adicionou = True
        if adicionou is False:
            self.__tela.vacina_nao_existe(fabricante)

    def excluir(self):
        dados_vacina = self.__tela.excluir_doses()

        fabricante = dados_vacina["fabricante"]
        qtd_doses = dados_vacina["qtd_doses"]
        vacina_atual = Vacina(fabricante, qtd_doses)
        excluiu = False

        for vacina in self.__vacinas:
            if vacina.fabricante == vacina_atual.fabricante:
                vacina.qtd_doses -= vacina_atual.qtd_doses
                if vacina.qtd_doses <= 0:
                    self.__vacinas.remove(vacina)
                excluiu = True
        if excluiu is False:
            self.__tela.vacina_nao_existe(fabricante)

    def alterar(self):
        dados_vacina = self.__tela.alterar_doses()

        fabricante = dados_vacina["fabricante"]
        qtd_doses = dados_vacina["qtd_doses"]
        vacina_atual = Vacina(fabricante, qtd_doses)
        alterou = False

        for vacina in self.__vacinas:
            if vacina.fabricante == vacina_atual.fabricante:
                vacina.qtd_doses = vacina_atual.qtd_doses
                alterou = True
        if alterou is False:
            self.__tela.vacina_nao_existe(fabricante)

    def qtd_doses_cada_fabricante(self):
        for vacina in self.__vacinas:
            self.__tela.mostrar_vacinas({"fabricante": vacina.fabricante, "quantidade de doses": vacina.qtd_doses})

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
        self.__continuar = False