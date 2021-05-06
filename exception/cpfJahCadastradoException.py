import PySimpleGUI as sg

class CpfJahCadastradoException(Exception):
    def __init__(self):
        sg.Popup("Já existe um cadastro com este CPF!")