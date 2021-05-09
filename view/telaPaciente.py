from view.abstractTela import AbstractTela
import PySimpleGUI as sg
from view.telaDadosPessoa import TelaDadosPessoa
from view.telaEndereço import TelaDadosEndereco

class TelaPaciente(AbstractTela):

    def __init__(self):
        self.__window = None
        self.init_components()
        self.__tela_dados_pessoa = TelaDadosPessoa()
        self.__tela_dados_endereco = TelaDadosEndereco()

    def init_components(self, pacientes=[]):
        layout = []
        for i in range(len(pacientes)):
            linha = [sg.Radio("{} - {} - {} - {} - {} - {}".format(pacientes[i][0], pacientes[i][1], pacientes[i][2], pacientes[i][3], pacientes[i][4], pacientes[i][5]), "paciente", size=(30, 1))]
            layout.append(linha)
        layout.append([sg.Button("Adicionar Paciente", key="1"), sg.Button("Alterar Dados", key="2"), sg.Button("Excluir", key="3")])
        self.__window = sg.Window("Pacientes").Layout(layout)

    def mostrar_menu(self, pacientes):
        self.init_components(pacientes)
        botao, valores = self.__window.Read()
        if botao is None:
            botao = 0
        cpf = None
        for i in range(len(valores.values())):
            if valores[i]:
                cpf = pacientes[i][2]
        self.close()
        return (int(botao), cpf)

    def popup(self,msg):
        sg.Popup("","{}".format(msg))

    def recebe_dados_paciente(self):
        return self.__tela_dados_pessoa.recebe_dados()

    def recebe_endereco_paciente(self):
        return  self.__tela_dados_endereco.recebe_dados()

    def close(self):
        self.__window.Close()
