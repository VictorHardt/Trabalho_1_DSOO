from view.telaEnfermeiro import TelaEnfermeiro
from model.enfermeiro import Enfermeiro
from model.paciente import Paciente
from persistence.enfermeiroDAO import EnfermeiroDAO
from exception.cpfJahCadastradoException import CpfJahCadastradoException

class ControladorEnfermeiro:
    def __init__(self):
        self.__tela = TelaEnfermeiro()
        self.__dao = EnfermeiroDAO()
        self.__continuar = True
        self.__enfermeiro = None
        
    def abre_tela(self):

        self.__continuar = True
        lista_opcoes = {
            1: self.cadastra_enfermeiro,
            2: self.altera_dados_enfermeiro,
            3: self.exlui_enfermeiro, 
            0: self.retorna}

        while self.__continuar:
            enfermeiros = self.__dao.get_all()
            tuplas = []
            for enfermeiro in enfermeiros:
                tuplas.append((enfermeiro.nome, enfermeiro.cpf))
            opcao_escolhida = self.__tela.mostrar_menu(tuplas)
            cpf = opcao_escolhida[1]
            if cpf:
                self.__enfermeiro = self.__dao.get(cpf)
            funcao_escolhida = lista_opcoes[opcao_escolhida[0]]
            funcao_escolhida()

    def cadastra_enfermeiro(self):

        dados_enfermeiro = self.__tela.recebe_dados_enfermeiro()
        if dados_enfermeiro is not 0:
            try:
                nome = dados_enfermeiro["nome"]
                cpf = dados_enfermeiro["cpf"]
                enfermeiro = self.__dao.get(cpf)
                if enfermeiro is None:
                    self.__dao.add(Enfermeiro(nome, cpf))
                    cadastrou = True
                    self.__tela.popup("Enfermeiro cadastrado com sucesso!")
                else:
                    raise CpfJahCadastradoException
            except CpfJahCadastradoException:
                pass
        else:
            pass

    def altera_dados_enfermeiro(self):
        
        dados_alteracao = self.__tela.recebe_dados_enfermeiro()

        if dados_alteracao is not 0:
            try:
                duplicado = False
                if self.__dao.get(dados_alteracao["cpf"]) is not None:
                    duplicado = True
                    raise CpfJahCadastradoException
                if not duplicado:
                    self.__enfermeiro.cpf = dados_alteracao["cpf"]
                    self.__enfermeiro.nome = dados_alteracao["nome"]
                    self.__tela.popup("Alterado com sucesso!")
                    self.__dao.update()
            except CpfJahCadastradoException:
                pass
        else:
            pass

    def exlui_enfermeiro(self):
        self.__dao.remove(self.__enfermeiro.cpf)

    def retorna(self):
        self.__continuar = False
