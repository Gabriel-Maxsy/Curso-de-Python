import abc

class Conta(abc.ABC):
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
        
    @abc.abstractmethod
    def sacar(self, valor):
        ...

    def depositar(self, valor):
        self.saldo += valor
        self.detalhes(f'(Deposito de {valor})')
    
    def detalhes(self, msg=''):
        print(f'O seu saldo é {self.saldo:.2f} {msg}')
        print('-' * 10)

class ContaPoupanca(Conta):
    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor

        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f'(Saque {valor})')
            return self.saldo
        
        print('Não foi possível sacar o valor desejado')
        self.detalhes(f'Saque negado {valor}')

if __name__ == '__main__':
    cp1 = ContaPoupanca(1, 2, 0)
    cp1.sacar(2)
    cp1.depositar(1)
    cp1.sacar(1)