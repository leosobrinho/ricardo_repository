
class SaldoInsuficienteException(Exception):
    def __init__(self, mensagem="Saldo insuficiente para a operação."):
        self.mensagem = mensagem
        super().__init__(self.mensagem)


class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado com sucesso. Saldo atual: R${self.saldo:.2f}")

    def sacar(self, valor):
        if valor > self.saldo:
            raise SaldoInsuficienteException(f"Tentativa de saque: R${valor:.2f}. Saldo disponível: R${self.saldo:.2f}")
        self.saldo -= valor
        print(f"Saque de R${valor:.2f} realizado com sucesso. Saldo atual: R${self.saldo:.2f}")


def main():
    conta = ContaBancaria("João", 100)

    try:
        conta.sacar(150)  
    except SaldoInsuficienteException as e:
        print(e)

    conta.depositar(50)  
    try:
        conta.sacar(100)  
    except SaldoInsuficienteException as e:
        print(e)

if __name__ == "__main__":
    main()
