from abc import ABC, abstractmethod

class AbstractTela(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def mostrar_menu(self):
        pass

    def ler_numero(self, lista_opcoes):
        pass