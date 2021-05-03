import PySimpleGUI as sg
from view.abstractTela import AbstractTela

class TelaSistema(AbstractTela):

    def __init__(self):
        self.__windown = None
        self.init_components()

    def init_components(self):
        layout = [[sg.Button("Tela de Pacientes", key="1", size=(20, 1))],
                  [sg.Button("Tela de Enfermeiros", key="2", size=(20, 1))],
                  [sg.Button("Tela de Vacinas", key="3", size=(20, 1))],
                  [sg.Button("Tela de Agendamentos", key="4", size=(20, 1))]]
        self.__window = sg.Window("Sistema de Vacinação").Layout(layout)

    def mostrar_menu(self):
        self.init_components()
        botao, valores = self.__window.Read()
        if botao is None:
            botao = 0
        return int(botao)

    def close(self):
        self.__window.close()