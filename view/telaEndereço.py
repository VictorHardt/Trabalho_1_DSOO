import PySimpleGUI as sg

class TelaDadosEndereco():
    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        layout = [
                    [sg.Text("Cidade", size=(10,0)), sg.InputText("", key="cidade")],
                    [sg.Text("Rua", size=(10,0)), sg.InputText("", key="rua")],
                    [sg.Text("Número", size=(10,0)), sg.InputText("", key="numero")],
                    [sg.Submit(), sg.Cancel()]
                ]

        self.__window = sg.Window("Cadastro de endereço").Layout(layout)

    def recebe_dados(self):
        self.init_components()
        continuar = True
        while continuar:
            botao, valores = self.__window.Read()
            if botao is None or botao is "Cancel":
                valores = 0
                continuar = False
            elif len(valores["cidade"]) > 0 and len(valores["rua"]) > 0 and len(valores["numero"]) > 0:
                valores["cidade"].strip().capitalize()
                valores["rua"].strip().capitalize()
                valores["numero"].strip().capitalize()
                continuar = False
        self.close()
        return valores

    def close(self):
        self.__window.Close()