import PySimpleGUI as sg

class LocalArmazenamentoJaCadastrado(Exception):
    def __init__(self):
        sg.Popup("O local de armazenamento já está cadastrado!")