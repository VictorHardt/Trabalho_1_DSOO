import PySimpleGUI as sg

class LocalArmazenamentoNaoCadastradoException(Exception):
    def __init__(self):
        sg.Popup("Local de armazenamento não existe. Cadastre o local de armazenamento!")