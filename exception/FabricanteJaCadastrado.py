import PySimpleGUI as sg

class FabricanteJaCadastrado(Exception):
    def __init__(self):
        sg.Popup("O fabricante já foi cadastrado!")