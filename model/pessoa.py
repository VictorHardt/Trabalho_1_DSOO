from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome: str, cpf: str):
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(cpf, str):
            self.__cpf = cpf

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome

    @property
    def cpf(self) -> int:
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf: int):
        if isinstance(cpf, int):
            self.__cpf = cpf