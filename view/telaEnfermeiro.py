import PySimpleGUI as sg
from view.abstractTela import AbstractTela
from view.telaDadosPessoa import TelaDadosPessoa

class TelaEnfermeiro(AbstractTela):

    def __init__(self):
        self.__windown = None
        self.init_components()
        self.__tela_dados_pessoa = TelaDadosPessoa()

    def init_components(self, enfermeiros=[]):

        layout = []
        for i in range(len(enfermeiros)):
            linha = [sg.Radio("{} - {}".format(enfermeiros[i][0], enfermeiros[i][1]), "enfermeiro")]
            layout.append(linha)
        layout.append([sg.Button("Adicionar Enfermeiro", key="1"), sg.Button("Alterar Dados", key="2"), sg.Button("Excluir", key="3")])
        self.__window = sg.Window("Enfermeiros").Layout(layout)

    def mostrar_menu(self, enfermeiros):
        
        self.init_components(enfermeiros)
        botao, valores = self.__window.Read()
        if botao is None:
            botao = 0
        cpf = None
        for i in range(len(valores.values())):
            if valores[i]:
                cpf = enfermeiros[i][1]
        self.close()
        return (int(botao), cpf)

    def popup(self,msg):
        sg.Popup("","{}".format(msg))

    def recebe_dados_enfermeiro(self):
        return self.__tela_dados_pessoa.recebe_dados()

    def close(self):
        self.__window.Close()
        