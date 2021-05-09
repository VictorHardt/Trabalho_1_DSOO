from model.paciente import Paciente
from view.telaPaciente import TelaPaciente
from model.endereco import Endereco
from persistence.pacienteDAO import PacienteDAO
from exception.cpfJahCadastradoException import CpfJahCadastradoException

class ControladorPaciente:
    def __init__(self):
        self.__dao_pacientes = PacienteDAO()
        self.__tela = TelaPaciente()
        self.__continuar = True
        self.__paciente = None

    def abre_tela(self):
        self.__continuar = True
        lista_opcoes = {1: self.cadastra_paciente, 2: self.altera_dados_paciente, 3: self.exclui_paciente, 0: self.retorna}

        while self.__continuar:
            pacientes = self.__dao_pacientes.get_all()
            tuplas = []
            for paciente in pacientes:
                tuplas.append((paciente.idade, paciente.nome, paciente.cpf, paciente.endereco.cidade, paciente.endereco.rua, paciente.endereco.numero))
            opcao_escolhida = self.__tela.mostrar_menu(tuplas)
            cpf = opcao_escolhida[1]
            if cpf:
                self.__paciente = self.__dao_pacientes.get(cpf)
            funcao_escolhida = lista_opcoes[opcao_escolhida[0]]
            funcao_escolhida()

    def cadastra_paciente(self):
        dados_paciente = self.__tela.recebe_dados_paciente()
        dados_endereco = self.__tela.recebe_endereco_paciente()

        if dados_paciente is not 0 and dados_endereco is not 0:
            try:
                nome = dados_paciente["nome"]
                cpf = dados_paciente["cpf"]
                idade = int(dados_paciente["idade"])
                cidade = dados_endereco["cidade"]
                rua = dados_endereco["rua"]
                numero = int(dados_endereco["numero"])

                paciente = self.__dao_pacientes.get(cpf)

                if paciente is None:
                    self.__dao_pacientes.add(Paciente(idade, nome, cpf, cidade, rua, numero))
                    self.__tela.popup("Paciente cadastrado com sucesso!")
                else:
                    raise CpfJahCadastradoException
            except CpfJahCadastradoException:
                pass
        else:
            pass

    def altera_dados_paciente(self):
        dados_paciente = self.__tela.recebe_dados_paciente()
        dados_endereco = self.__tela.recebe_endereco_paciente()

        if dados_paciente is not 0 and dados_endereco is not 0:
            try:
                duplicado = False
                if self.__dao_pacientes.get(dados_paciente["cpf"]) is not None:
                    duplicado = True
                    raise CpfJahCadastradoException
                if not duplicado:
                    self.__paciente.nome = dados_paciente["nome"]
                    # self.__paciente.cpf = dados_paciente["cpf"]
                    self.__paciente.idade = int(dados_paciente["idade"])
                    self.__paciente.endereco.cidade = dados_endereco["cidade"]
                    self.__paciente.endereco.rua = dados_endereco["rua"]
                    self.__paciente.endereco.numero = int(dados_endereco["numero"])
                    self.__tela.popup("Alterado com sucesso!")
                    self.__dao_pacientes.update()
            except CpfJahCadastradoException:
                pass
        else:
            pass

    def exclui_paciente(self):
        self.__dao_pacientes.remove(self.__paciente.cpf)

    def retorna_paciente(self, cpf:str) -> Paciente:
        return self.__dao_pacientes.get(cpf)

    def retorna(self):
        self.__continuar = False