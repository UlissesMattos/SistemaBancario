from abc import ABC, abstractmethod

class Conta:
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    def detalhes(self):
        print(f'Agencia: {self.agencia} \n Conta: {self.conta} \n Saldo: {self.saldo}')

    def depositar(self, valor):
        self.saldo += valor
        self.detalhes()

    @abstractmethod
    def sacar(self, valor):
        pass


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=100):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            print('Saldo insuficiente.')
        else:
            self.saldo -= valor
            self.detalhes()


class ContaPoupanca(Conta):
    def __init__(self, agencia, conta, saldo):
        super().__init__(agencia, conta, saldo)

    def sacar(self, valor):
        if self.saldo < valor:
            print('Saldo insuficiente.')
        else:
            self.saldo -= valor
            self.detalhes()
