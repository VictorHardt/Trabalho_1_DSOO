from model.vacina import Vacina
from view.telaVacina import TelaVacina
from model.localArmazenamento import LocalArmazenamento
from persistence.vacinaDAO import VacinaDAO
from persistence.localArmazenamentoDAO import LocalArmazenamentoDAO
from exception.cpfJahCadastradoException import CpfJahCadastradoException
from exception.LocalArmazenamentoNaoCadastradoException import LocalArmazenamentoNaoCadastradoException
from exception.FabricanteJaCadastrado import FabricanteJaCadastrado
from exception.LocalArmazenamentoJaCadastrado import LocalArmazenamentoJaCadastrado

class ControladorVacina:
    def __init__(self):
        self.__dao = VacinaDAO()
        self.__tela = TelaVacina()
        self.__continuar = True
        self.__dao_locais_armazenamento = LocalArmazenamentoDAO()
        self.__vacina = None

    def abre_tela(self):
        self.__continuar = True
        lista_opcoes = {
            1: self.cadastra_vacina,
            2: self.alterar,
            3: self.cadastrar_local_armazenamento,
            4: self.excluir,
            0: self.retorna}

        while self.__continuar:
            vacinas = self.__dao.get_all()
            tuplas = []
            for vacina in vacinas:
                tuplas.append((vacina.fabricante, vacina.qtd_doses, vacina.local_armazenamento))
            opcao_escolhida = self.__tela.mostrar_menu(tuplas)
            fabricante = opcao_escolhida[1]
            if fabricante:
                self.__vacina = self.__dao.get(fabricante)
            funcao_escolhida = lista_opcoes[opcao_escolhida[0]]
            funcao_escolhida()

    def cadastra_vacina(self):
        dados_vacina = self.__tela.recebe_dados_vacina()

        if dados_vacina is not 0:
            try:
                fabricante = dados_vacina["fabricante"]
                qtd_doses = int(dados_vacina["qtd_doses"])
                local_armazenamento = dados_vacina["local_armazenamento"]

                vacina = self.__dao.get(fabricante)

                local_armazenamento_atual = self.__dao_locais_armazenamento.get(local_armazenamento)

                if vacina is None and local_armazenamento_atual is not None:
                    self.__dao.add(Vacina(fabricante, qtd_doses, local_armazenamento))
                    self.__tela.popup("Vacina cadastrada com sucesso!")
                elif local_armazenamento_atual is None:
                    raise LocalArmazenamentoNaoCadastradoException
                else:
                    raise FabricanteJaCadastrado
            except FabricanteJaCadastrado:
                pass
            except LocalArmazenamentoNaoCadastradoException:
                pass
        else:
            pass

    def cadastrar_local_armazenamento(self):
        dados_local_armazenamento = self.__tela.recebe_dados_local_armazenamento()

        if dados_local_armazenamento is not 0:
            try:
                local_armazenamento = dados_local_armazenamento["local_armazenamento"]
                temperatura = int(dados_local_armazenamento["temperatura"])

                local_armazenamento_atual = self.__dao_locais_armazenamento.get(local_armazenamento)

                if local_armazenamento_atual is None:
                    self.__dao_locais_armazenamento.add(LocalArmazenamento(local_armazenamento, temperatura))
                    self.__tela.popup("Local de armazenamento cadastrado com sucesso!")
                else:
                    raise LocalArmazenamentoJaCadastrado
            except LocalArmazenamentoJaCadastrado:
                pass
        else:
            pass

    def excluir(self):
        self.__dao.remove(self.__vacina.fabricante)

    def alterar(self):
        dados_vacina = self.__tela.recebe_dados_vacina()

        if dados_vacina is not 0:
            try:
                local_armazenamento = dados_vacina["local_armazenamento"]
                local_armazenamento_atual = self.__dao_locais_armazenamento.get(local_armazenamento)

                duplicado = False
                if self.__dao.get(dados_vacina["fabricante"]) is not None:
                    duplicado = True
                    raise CpfJahCadastradoException
                elif local_armazenamento_atual is None:
                    duplicado = True
                    raise LocalArmazenamentoNaoCadastradoException
                if not duplicado:
                    self.__dao.remove(self.__vacina.fabricante)
                    self.__vacina.fabricante = dados_vacina["fabricante"]
                    self.__vacina.qtd_doses = int(dados_vacina["qtd_doses"])
                    self.__vacina.local_armazenamento = dados_vacina["local_armazenamento"]
                    self.__tela.popup("Alterado com sucesso!")
                    self.__dao.add(self.__vacina)
            except CpfJahCadastradoException:
                pass
            except LocalArmazenamentoNaoCadastradoException:
                pass
        else:
            pass

    def retorna_vacina_para_agendamento(self):

        vacina = None
        vacinas = list(self.__dao.get_all())
        i = 0
        while vacina is None and i < len(vacinas):
            if vacinas[i].qtd_doses >= 2:
                vacina = vacinas[i]
                vacina.qtd_doses -= 2
        return vacina

    def retorna(self):
        self.__continuar = False