from model.paciente import Paciente
from view.telaPaciente import TelaPaciente
from model.endereco import Endereco
from persistence.pacienteDAO import PacienteDAO

class ControladorPaciente:
    def __init__(self):
        self.__dao_pacientes = PacienteDAO()
        self.__tela = TelaPaciente()
        self.__continuar = True

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_paciente, 2: self.altera_dados_paciente, 3: self.exclui_paciente, 4:self.lista_pacientes, 0: self.retorna}
        self.__continuar = True        

        while self.__continuar:
            opcao_escolhida = self.__tela.mostrar_menu()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def cadastra_paciente(self):
        dados_paciente = self.__tela.recebe_dados_paciente()
        endereco = dados_paciente["endereco"]

        paciente = Paciente(dados_paciente["idade"], dados_paciente["nome"], dados_paciente["CPF"], endereco["cidade"], endereco["rua"], endereco["numero"])

        duplicado = False
        for i in self.__dao_pacientes.get_all():
            if i.cpf == paciente.cpf:
                self.__tela.cpf_duplicado_error(paciente.cpf)
                duplicado = True
        if not duplicado:
            self.__dao_pacientes.add(paciente)

    def altera_dados_paciente(self):
        dados_paciente = self.__tela.alterar()

        idade = dados_paciente["idade"]
        nome = dados_paciente["nome"]
        CPF = dados_paciente["CPF"]
        endereco = dados_paciente["endereco"]
        cidade = endereco["cidade"]
        rua = endereco["rua"]
        numero = endereco["numero"]

        paciente_atual = Paciente(idade, nome, CPF, cidade, rua, numero)

        alterou = False

        for pac in self.__dao_pacientes.get_all():
            if pac.cpf == paciente_atual.cpf:
                alterou = True
        if alterou is False:
            self.__tela.cpf_nao_existe(paciente_atual.cpf)

        if alterou is True:
            self.__dao_pacientes.remove(pac.cpf)
            self.__dao_pacientes.add(Paciente(idade, nome, CPF, cidade, rua, numero))


    def exclui_paciente(self):
        dados_paciente = self.__tela.excluir_paciente()
        cpf_atual = dados_paciente["CPF"]
        excluiu = False
        excluiu_paciente = False

        for paciente in self.__dao_pacientes.get_all():
            if paciente.cpf == cpf_atual:
                excluiu_paciente = True
            excluiu = True

        if excluiu is False:
            self.__tela.cpf_nao_existe(cpf_atual)

        if excluiu_paciente is True:
            self.__dao_pacientes.remove(dados_paciente["CPF"])


    def retorna_paciente(self, cpf:str) -> Paciente:
        pac = None
        for paciente in self.__dao_pacientes.get_all():
            if paciente.cpf == cpf:
                pac = paciente
        return pac

    def lista_pacientes(self):
        for paciente in self.__dao_pacientes.get_all():
            self.__tela.listar_pacientes({"idade": paciente.idade, "nome": paciente.nome, "CPF": paciente.cpf,
                                             "cidade": paciente.endereco.cidade, "rua": paciente.endereco.rua, 
                                             "numero": paciente.endereco.numero})

    def retorna(self):
        self.__continuar = False