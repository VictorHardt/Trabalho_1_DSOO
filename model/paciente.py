from model.pessoa import Pessoa
from model.endereco import Endereco

class Paciente(Pessoa):
    def __init__(self, idade: int, nome: str, cpf: str, cidade: str, rua: str, numero: int):
        if isinstance(nome, str) and isinstance(cpf, str):
            super().__init__(nome, cpf)
        if isinstance(idade, int):
            self.__idade = idade
        if isinstance(cidade, str) and isinstance(rua, str) and isinstance(numero, int):
            self.__endereco = Endereco(cidade, rua, numero)

    @property
    def idade(self) -> int:
        return self.__idade

    @idade.setter
    def idade(self, idade: int):
        if isinstance(idade, int):
            self.__idade = idade
