from model.vacina import Vacina
from view.telaVacina import TelaVacina
from model.localArmazenamento import LocalArmazenamento
from persistence.vacinaDAO import VacinaDAO
from persistence.localArmazenamentoDAO import LocalArmazenamentoDAO

class ControladorVacina:
    def __init__(self):
        self.__dao = VacinaDAO()
        self.__tela = TelaVacina()
        self.__continuar = True
        self.__dao_locais_armazenamento = LocalArmazenamentoDAO()

    def abre_tela(self):
        self.__continuar = True
        lista_opcoes = {
            1: self.cadastra_vacina,
            2: self.add_doses,
            3: self.excluir,
            4: self.alterar,
            5: self.qtd_doses_cada_fabricante,
            6: self.cadastra_local_armazenamento,
            0: self.retorna}

        while self.__continuar:
            opcao_escolhida = self.__tela.mostrar_menu()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def cadastra_vacina(self):

        cadastrou = False
        while not cadastrou:
            dados_vacina = self.__tela.recebe_dados_vacina()
            fabricante = dados_vacina["fabricante"]
            qtd_doses = dados_vacina["qtd_doses"]
            local_armazenamento = dados_vacina["local_armazenamento"]


            local_atual = self.__dao_locais_armazenamento.get(local_armazenamento)
            vacina_atual = self.__dao.get(fabricante)

            if local_atual is None:
                self.__tela.local_armazenamento_nao_cadastrado(local_armazenamento)
            elif vacina_atual is None and local_atual is not None:
                self.__dao.add(Vacina(fabricante, qtd_doses, local_armazenamento))
                cadastrou = True
            else:
                self.__tela.vacina_repetida(fabricante)



    def add_doses(self):
        dados_vacina = self.__tela.adiconar_doses()

        fabricante = dados_vacina["fabricante"]
        qtd_doses = dados_vacina["qtd_doses"]

        vacina_atual = Vacina(fabricante, qtd_doses)
        adicionou = False

        for vacina in self.__dao.get_all():
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
        excluiu_fabricante = False

        for vacina in self.__dao.get_all():
            if vacina.fabricante == vacina_atual.fabricante:
                vacina.qtd_doses -= vacina_atual.qtd_doses
                if vacina.qtd_doses <= 0:
                    excluiu_fabricante = True
                excluiu = True
        if excluiu is False:
            self.__tela.vacina_nao_existe(fabricante)
        if excluiu_fabricante is True:
            self.__dao.remove(dados_vacina["fabricante"])


    def alterar(self):
        dados_vacina = self.__tela.alterar_doses()

        fabricante = dados_vacina["fabricante"]
        qtd_doses = dados_vacina["qtd_doses"]
        vacina_atual = Vacina(fabricante, qtd_doses)
        alterou = False

        for vacina in self.__dao.get_all():
            if vacina.fabricante == vacina_atual.fabricante:
                vacina.qtd_doses = vacina_atual.qtd_doses
                alterou = True
        if alterou is False:
            self.__tela.vacina_nao_existe(fabricante)

    def qtd_doses_cada_fabricante(self):
        for vacina in self.__dao.get_all():
            self.__tela.mostrar_vacinas({"fabricante": vacina.fabricante, "quantidade de doses": vacina.qtd_doses})

    def cadastra_local_armazenamento(self):
        dados_armazenamento = self.__tela.recebe_dados_amazenamento()
        local_armazenamento = LocalArmazenamento(dados_armazenamento["local_armazenamento"], dados_armazenamento["temperatura"])
        locais_armazenamento = self.__dao_locais_armazenamento.get_all()

        duplicado = False
        for local_armz in locais_armazenamento:
            if local_armazenamento.local == local_armz.local:
                duplicado = True
        if duplicado:
            self.__tela.local_armazenamento_ja_cadastrado(local_armazenamento.local)
        else:
            self.__dao_locais_armazenamento.add(local_armazenamento)


    def retorna_vacina_para_agendamento(self):

        vacina = None
        i = 0
        while vacina is None and i < len(self.__vacinas):
            if self.__vacinas[i].qtd_doses >= 2:
                vacina = self.__vacinas[i]
                vacina.qtd_doses -= 2
        return vacina

    def retorna(self):
        self.__continuar = False