from datetime import datetime
import pytz
from random import randint

class ContaCorrente:
    """
    Isto é um help da tua classe.
    É interessante conter os atributos e métodos da tua classe.
    Siga o PEP 257
    """

    @staticmethod
    def _data_hora():
        fuso_br = pytz.timezone('Brazil/East')
        return datetime.now(fuso_br).strftime(r"%d/%m/%Y, %H:%M:%S")
    

    def __init__(self,nome,cpf, agencia, numConta):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0.0
        self.limite = None
        self.agencia = agencia
        self.numero_Conta = numConta
        self.transacoes = []
        self.cartoes = []

    def consultar_saldo(self):
        print(f'Seu saldo é de R${self.saldo:.2f}')

    def depositar(self,valor):
        self.saldo += valor
        self.transacoes.append(("Depósito",valor,self.saldo,self._data_hora()))

    def _limite_conta(self):#essa função é tão inútil quanto a ONU
        self.limite = -1000
        return self.limite
    
    def consultar_limite_cheque_especial(self):
        print(f'Seu limite de cheque especial é R${self._limite_conta:.2f}')
    
    def sacar_dinheiro(self,valor):
        if self.saldo-valor<self._limite_conta():
            print("Saldo insuficiente para a operação")
            self.consultar_saldo
        else:
            self.saldo -= valor
            self.transacoes.append(("Saque",valor,self.saldo,self._data_hora()))

    def visualizar_historico_transacoes(self):
        print("histórico de transações")        
        for transacao in self.transacoes:
            print(transacao)

    def transferir(self, valor,conta_destino):
        self.saldo -= valor
        self.transacoes.append(("Transferencia efetuada",valor,self.saldo,self._data_hora()))
        conta_destino.saldo += valor
        conta_destino.transacoes.append(("Tranferência recebida",valor,conta_destino.saldo,conta_destino._data_hora()))


class CartaoCredito:

    @staticmethod
    def _data_hora():
        fuso_br = pytz.timezone('Brazil/East')
        return datetime.now(fuso_br)
    
    def __init__(self, titular,conta_corrente):
        self.numero = f"{randint(1000,9999)}.{randint(1000,9999)}.{randint(1000,9999)}.{randint(1000,9999)}"
        self.titular = titular
        self.validade = f"{self._data_hora().month}/{self._data_hora().year+4}"
        self.cod_seguranca = f'{randint(0,9)}{randint(0,9)}{randint(0,9)}'
        self._senha = '1234'
        self.limite = 1000
        self.conta_corrente = conta_corrente
        conta_corrente.cartoes.append(self)

    @property
    def senha(self):
        return self._senha
    
    @senha.setter
    def senha(self,valor:str):
        if len(valor) == 4 and valor.isnumeric():
            self._senha = valor
        else:
            print("Nova senha inválida!")
