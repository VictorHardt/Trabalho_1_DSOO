class Endereco:
    def __init__(self, cidade: str, rua: str, numero: int):
        if isinstance(numero, int):
            self.__numero = numero
        if isinstance(rua, str):
            self.__rua = rua
        if isinstance(cidade, str):
            self.__cidade = cidade

    @property
    def numero(self) -> int:
        return self.__numero

    @numero.setter
    def numero(self, numero: int):
        if isinstance(numero, int):
            self.__numero = numero

    @property
    def rua(self) -> str:
        return self.__rua

    @rua.setter
    def rua(self, rua: str):
        if isinstance(rua, str):
            self.__rua = rua

    @property
    def cidade(self) -> str:
        return self.__cidade

    @cidade.setter
    def cidade(self, cidade: str):
        if isinstance(cidade, str):
            self.__cidade = cidade
