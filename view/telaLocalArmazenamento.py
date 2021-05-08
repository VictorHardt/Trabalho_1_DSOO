import PySimpleGUI as sg

class TelaLocalArmazenamento():
    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        layout = [
                    [sg.Text("Local de armazenamento", size=(10,0)), sg.InputText("", key="local_armazenamento")],
                    [sg.Text("Temperatura", size=(10,0)), sg.InputText("", key="temperatura")],
                    [sg.Submit(), sg.Cancel()]
                 ]
        self.__window = sg.Window("Registro de local de armazenamento").Layout(layout)

    def recebe_dados(self):
        self.init_components()
        continuar = True
        while continuar:
            botao, valores = self.__window.Read()
            if botao is None or botao is "Cancel":
                valores = 0
                continuar = False
            elif len(valores["local_armazenamento"]) > 0 and len(valores["temperatura"]) > 0:
                valores["local_armazenamento"].strip().capitalize()
                valores["temperatura"].strip().capitalize()
                continuar = False
        self.close()
        return valores

    def close(self):
        self.__window.Close()