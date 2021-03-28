from model.vacina import Vacina
from view.telaVacina import TelaVacina

class ControladorVacina:
    def __init__(self, controlador_sistema: Controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__vacinas = []
        self.__tela = TelaVacina(self)

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_vacina, 2: self.add_doses, 3: self.excluir, 4: self.alterar, 5: self.qtd_doses_cada_fabricante, 0: self.retorna}

        while True:
            opcao_escolhida = self.__tela.mostrar_menu()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def cadastra_vacina(self, fabricante: str, quantidade: int):
        if isinstance(fabricante, str):
            self.__fabricante = fabricante
        if isinstance(quantidade, int):
            self.__quantidade = quantidade

        pass

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

    def retorna(self):
        pass