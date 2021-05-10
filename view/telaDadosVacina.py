import PySimpleGUI as sg

class TelaDadosVacina():
    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        layout = [
                    [sg.Text("Fabricante", size=(10,0)), sg.InputText("", key="fabricante")],
                    [sg.Text("Quantidade de doses", size=(10,0)), sg.InputText("", key="qtd_doses")],
                    [sg.Text("Local de armazenamento", size=(10, 0)), sg.InputText("", key="local_armazenamento")],
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
            elif len(valores["fabricante"]) > 0 and len(valores["qtd_doses"]) > 0 and len(valores["local_armazenamento"]) > 0:
                valores["fabricante"] = valores["fabricante"].strip().capitalize()
                valores["qtd_doses"] = valores["qtd_doses"].strip()
                valores["local_armazenamento"] = valores["local_armazenamento"].strip().capitalize()
                continuar = False
        self.close()
        return valores

    def close(self):
        self.__window.Close()