class LocalArmazenamento:
    def __init__(self, local: str, temperatura: int):
        if isinstance(local, str):
            self.__local = local
        if isinstance(temperatura, int):
            self.__temperatura = temperatura
        
    @property
    def local(self) -> str:
        return self.__local

    @local.setter
    def local(self, local: str):
        if isinstance(local, str):
            self.__local = local

    @property
    def temperatura(self) -> int:
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, temperatura: int):
        if isinstance(temperatura, int):
            self.__temperatura = temperatura
