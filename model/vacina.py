from model.localArmazenamento import LocalArmazenamento

class Vacina:
    def __init__(self, fabricante: str, qtd_doses: int, local_armazenamento: str):
        if isinstance(fabricante, str):
            self.__fabricante = fabricante
        if isinstance(qtd_doses, int):
            self.__qtd_doses = qtd_doses
        if isinstance(local_armazenamento, str):
            self.__local_armazenamento = local_armazenamento

    @property
    def fabricante(self) -> str:
        return self.__fabricante

    @fabricante.setter
    def fabricante(self, fabricante: str):
        if isinstance(fabricante, str):
            self.__fabricante = fabricante

    @property
    def qtd_doses(self) -> int:
        return self.__qtd_doses

    @qtd_doses.setter
    def qtd_doses(self, qtd_doses: int):
        if isinstance(qtd_doses, int):
            self.__qtd_doses = qtd_doses

    @property
    def local_armazenamento(self) -> str:
        return self.__local_armazenamento

    @local_armazenamento.setter
    def local_armazenamento(self, local_armazenamento: str):
        if isinstance(local_armazenamento, str):
            self.__local_armazenamento = local_armazenamento
