from view.abstractTela import AbstractTela

class TelaAgendamento(AbstractTela):

    def __init__(self):
        pass
        
    def mostrar_menu(self):

        print("")
        print("------------Menu de Agendamentos------------")
        print("")
        print("1 : Novo Agendamento")
        print("2 : Checa Agendamento")
        print("3 : Remove Agendamento")
        print("4 : Checa Agendamento")
        print("5 : Altera Agendamento")
        print("0 : Retornar")
        print("")

        return self.ler_numero([1,2,3,4,0])

    