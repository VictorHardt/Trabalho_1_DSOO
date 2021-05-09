from view.abstractTela import AbstractTela
import PySimpleGUI as sg
from view.telaDadosVacina import TelaDadosVacina
from view.telaLocalArmazenamento import TelaLocalArmazenamento

class TelaVacina(AbstractTela):

    def __init__(self):
        self.__window = None
        self.init_components()
        self.__tela_dados_vacina = TelaDadosVacina
        self.__tela_dados_local_armazenamento = TelaLocalArmazenamento

    def init_components(self, vacinas=[]):
        layout = []
        for i in range(len(vacinas)):
            linha = [sg.Radio("{} - {} - {}".format(vacinas[i][0], vacinas[i][1], vacinas[i][2]), "vacina", size=(30, 1))]
            layout.append(linha)
        layout.append([sg.Button("Adicionar vacina", key="1"), sg.Button("Alterar Dados", key="2"), sg.Button("Cadastrar local de armazenamento", key="3"), sg.Button("Excluir", key="4")])
        self.__window = sg.Window("Vacinas").Layout(layout)

    def mostrar_menu(self, vacinas):
        self.init_components(vacinas)
        botao, valores = self.__window.Read()
        if botao is None:
            botao = 0
        fabricante = None
        for i in range(len(valores.values())):
            if valores[i]:
                fabricante = vacinas[i][0]
        self.close()
        return (int(botao), fabricante)

    def popup(self,msg):
        sg.Popup("","{}".format(msg))

    def recebe_dados_vacina(self):
        return self.__tela_dados_vacina().recebe_dados()

    def recebe_dados_local_armazenamento(self):
        return self.__tela_dados_local_armazenamento().recebe_dados()

    def close(self):
        self.__window.Close()

