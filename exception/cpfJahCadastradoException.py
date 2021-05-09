import PySimpleGUI as sg

class CpfJahCadastradoException(Exception):
    def __init__(self):
        sg.Popup("ERRO","Já existe um cadastro com este CPF!")