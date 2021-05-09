import PySimpleGUI as sg

class EnfermeiroNaoSelecionadoException(Exception):
    def __init__(self):
        sg.Popup("ERRO", "Selecione um enfermeiro!")