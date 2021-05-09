import PySimpleGUI as sg

class AgendamentoNaoSelecionadoException(Exception):
    def __init__(self):
        sg.Popup("ERRO", "Selecione um agendamento!")