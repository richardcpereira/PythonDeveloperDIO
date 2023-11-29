rom abc import ABC, abstractmethod
import datetime

class Transacao(ABC):
    @abstractmethod
    def deposito(self):
        pass
 
    @abstractmethod
    def saque(self):
        pass
 
 
class Pessoa_Física:
    def __init__(self, nome: str, cpf: int, dt_nascimento: str):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = dt_nascimento
 
 
class Pessoa_Juridica:
    def __init__(self, nome: str, cnpj: int, dt_nascimento: str ):
        self.nome = nome
        self.cnpj = cnpj
        self.data_nascimento = dt_nascimento
 
# =-=-=-=-=-==-=-=-=-=-==-=-=-=-=-==-=-=-=-=-==-=-=-=-=-==-=-=-=-=-=
 
class Cliente:
    def __init__(self, endereco: str):
        self.endereco = endereco
        self.contas = list()
        self.classificacao = '' # vai receber as classes pessoa fisica ou juridica
    
    @property
    def classificacao(self):
        return self.classificacao
    
    @classificacao.setter
    def classificacao(self, dados):
        self.classificacao = dados
    
    def adicionar_conta(self, conta):
        self.contas.append(conta)
 
    def realizar_transacao(self, numero, senha, transacao):
        for conta in self.contas:
            if conta.__numero == numero and conta.__senha == senha:
                match transacao:
                    case 'saque':
                        conta.__sacar()
                    case 'deposito':
                        conta.__depositar()
        
 
 
# =-=-=-=-=-==-=-=-=-=-==-=-=-=-=-==-=-=-=-=-==-=-=-=-=-==-=-=-=-=-=
 
class Conta:
    def __init__(self, cliente, senha,  historico, numero: int,  agencia = '00055', saldo = 0):
        self.__numero = numero
        self.__agencia = agencia
        self.__saldo = saldo
        self.__cliente = cliente #recebe a classe Cliente
        self.__historico = historico #recebe a classe Historico
        self.__senha = senha
 
    def __exibir_saldo(self):
        return self.saldo
 
# =-=-=-=-=-==-=-=-=-=-==-=-=-=-=-==-=-=-=-=-==-=-=-=-=-==-=-=-=-=-=
class Conta_Corrente(Conta):
    def __init__(self, limite = 15.000, limite_saque = 3, **kwargs):
        super().__init__(**kwargs)
        self.limite = limite
        self.limite_de_saque = limite_saque
 
    def __sacar(self, valor: float) -> bool:
        match len(self.__historico.registros):
            case self.limite_de_saque:
                print('Você já atingiu o limite de saques diários!')
            case _:
                if valor <= self.__saldo and valor != 0:
                    self.__saldo -= valor
                    self.__historico.adicionar_transacao(Transacao_Bancaria.saque(valor))

 
    def __depositar(self, valor: float) -> bool:
        total = self.__saldo + valor
        if total < self.limite  and valor != 0 or total == self.limite and valor !=0:
            self.__saldo += valor
            self.__historico.adicionar_transacao(Transacao_Bancaria.deposito(valor))

 
    @classmethod
    def gerar_conta(cls, numero: int, cliente):
        return cls(numero, cliente)
    
# =-=-=-=-=-==-=-=-=-=-==-=-=-=-=-==-=-=-=-=-==-=-=-=-=-==-=-=-=-=-=
 
class Transacao_Bancaria(Transacao):
    def __init__(self):
        self.transacao = {}
    
    def deposito(self, valor):
        self.transacao.setdefault({'Tipo de Transação': 'Depósito', 'Valor Depositado': f'R$ {valor}', 'Data da Transação': '{datetime.datetime.now().strftime("Data: %d/%m/%Y | Hora: %H:%M")}'})
    
 
    def saque(self, valor):
        self.transacao.setdefault({'Tipo de Transação': 'Saque', 'Valor do Saque': f'R$ {valor}', 'Data da Transação': '{datetime.datetime.now().strftime("Data: %d/%m/%Y | Hora: %H:%M")}'})
        
 
 
class Historico:
    def __init__(self):
        self.registros = [] # vai receber a classe Transacao_Bancaria
    
    def adicionar_transacao(self, transacao):
        self.registros.append(transacao)