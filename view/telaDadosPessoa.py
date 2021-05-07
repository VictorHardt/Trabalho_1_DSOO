import PySimpleGUI as sg

class TelaDadosPessoa():
    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        layout = [
                    [sg.Text("Nome", size=(10,0)), sg.InputText("", key="nome")],
                    [sg.Text("Cpf", size=(10,0)), sg.InputText("", key="cpf")],
                    [sg.Text("Idade", size=(10, 0)), sg.InputText("", key="idade")],
                    [sg.Submit(), sg.Cancel()]
                 ]
        self.__window = sg.Window("Cadastro").Layout(layout)

    def recebe_dados(self):
        self.init_components()
        continuar = True
        while continuar:
            botao, valores = self.__window.Read()
            if botao is None or botao is "Cancel":
                valores = 0
                continuar = False
            elif len(valores["nome"]) > 0 and len(valores["cpf"]) > 0 and len(valores["idade"]) > 0:
                valores["nome"].strip().capitalize()
                valores["cpf"].strip().capitalize()
                valores["idade"].strip().capitalize()
                continuar = False
        self.close()
        return valores

    def close(self):
        self.__window.Close()