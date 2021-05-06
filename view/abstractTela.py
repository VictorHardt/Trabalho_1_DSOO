from abc import ABC, abstractmethod

class AbstractTela(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def mostrar_menu(self):
        pass

    def ler_numero(self, inteiros_validos: [] = None, msg: str = "" ):

        while True:
            valor_lido = input(msg)
            try:
                inteiro = int(valor_lido)
                if inteiros_validos and inteiro not in inteiros_validos:
                    raise ValueError
                return inteiro
            except ValueError:
                print("Valor incorreto: Digite um valor numérico válido!")
                if inteiros_validos:
                    print("Valores validos: ", inteiros_validos)

    def ler_string(self, msg: str = ""):

        while True:
            string = input(msg)
            try:
                string = string.strip().capitalize()
                if len(string) == 0:
                    raise ValueError 
                return string
            except ValueError:
                print("Digite algo válido!")
