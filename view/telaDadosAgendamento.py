from datetime import date
import PySimpleGUI as sg

class TelaDadosAgendamento:
    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        layout = [
                    [sg.Text("Cpf do Enfermeiro", size=(10,0)), sg.InputText("", key="cpf_enf")],
                    [sg.Text("Cpf do Paciente", size=(10,0)), sg.InputText("", key="cpf")],
                    [sg.Text("Dia:", size=(5,0)), sg.Spin(values=('1', '2', '3','4','5','6','7','8','9','10',"11",'12','13','14','15','16','17','18',"19","20",'21','22','23','24','25', '26','27', '28', '29', '30', '31'), initial_value='1', key="dia")],
                    [sg.Text("Mês:", size=(5,0)), sg.Spin(values=('1', '2', '3','4','5','6','7','8','9','10',"11",'12'), initial_value='1', key="mes")],
                    [sg.Text("Ano:", size=(5,0)), sg.Spin(values=('2021','2022','2023','2024'), initial_value='2021', key="ano")],
                    [sg.Text("Hora:", size=(5,0)), sg.Spin(values=('8','9','10',"11",'12','13','14','15','16','17','18'), initial_value='8', key="hora")],
                    [sg.Button("Primeira Dose", key='1'), sg.Button("Segunda Dose", key='2'), sg.Cancel()]
                 ]
        self.__window = sg.Window("Novo Agendamento").Layout(layout)

    def recebe_dados(self):
        self.init_components()
        continuar = True
        while continuar:
            botao, valores = self.__window.Read()
            if botao is None or botao is "Cancel":
                valores = 0
                botao = 0
                continuar = False
            elif len(valores["cpf_enf"]) > 0 and len(valores["cpf"]) > 0 and len(valores["hora"]) > 0:
                try:
                    valores["cpf_enfermeiro"] = (valores["cpf_enf"]).strip()
                    valores["cpf"] = valores["cpf"].strip()
                    valores["hora"] = int(valores["hora"])
                    valores['data'] = date(int(valores['ano']), int(valores['mes']), int(valores['dia']))
                    continuar = False
                except Exception:
                    sg.Popup("", "DATA INVÁLIDA!")
                    continuar = True
        self.close()
        return (int(botao), valores)

    def close(self):
        self.__window.Close()