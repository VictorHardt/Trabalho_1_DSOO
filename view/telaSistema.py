from view.abstractTela import AbstractTela

class TelaSistema(AbstractTela):
    def __init__(self):
        pass

    def mostrar_menu(self):

        print("")
        print("------------Sistema de Vacinação------------")
        print("")
        print("1 : Tela de Pacientes")
        print("2 : Tela de Enfermeiros")
        print("3 : Tela de Vacinas")
        print("4 : Tela de Agendamentos")
        print("0 : Sair")
        print("")

        return self.ler_numero([1,2,3,4,0])